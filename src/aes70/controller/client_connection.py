import asyncio

from aes70.controller.remote_error import RemoteError
from aes70.connection import Connection
from aes70.ocp1.response import Response
from aes70.ocp1.keepalive import KeepAlive
from aes70.ocp1.notification import Notification
from aes70.controller.arguments import Arguments
from concurrent.futures import Future

class PendingCommand:
    @property
    def handle(self):
        return self.command.handle

    def __init__(self, resolve, reject, return_types, command):
        self.resolve = resolve
        self.reject = reject
        self.return_types = return_types
        self.command = command
        self.last_sent = 0
        self.retries = 0

    def response(self, o):
        resolve, reject, return_types, command = self.resolve, self.reject, self.return_types, self.command

        if o.status_code != 0:
            reject(RemoteError(o.status_code, command))
        elif not return_types:
            resolve(o)
        else:
            try:
                #print("@@@@ delivering a response with return values")

                length = min(o.param_count, len(return_types))
                #print("length of return types: ", length)
                if length == 0:
                    resolve()
                else:
                    result = [None] * length
                    data_view = bytearray(o.parameters)
                    #print("=> data_view: ", data_view)
                    pos = 0
                    for i in range(length):
                        #print("return_type: ", return_types[i])
                        pos, tmp = return_types[i].decode_from(data_view, pos)
                        result[i] = tmp
                    #print("results: ", result);
                    resolve(result[0] if length == 1 else Arguments(result))
            except Exception as err:
                reject(err)

def event_to_key(event):
    ono = event.emitter_o_no
    id = event.event_id

    return f"{ono},{id.def_level},{id.event_index}"


class ClientConnection(Connection):
    def __init__(self, options):
        super().__init__(options)
        self._pending_commands = {}
        self._next_command_handle = 0
        self._subscribers = {}

    def cleanup(self):
        super().cleanup()
        self._subscribers = None

        pending_commands = self._pending_commands
        self._pending_commands = None
        e = Exception('closed')
        for pending_command in pending_commands.values():
            pending_command.reject(e)

    def _add_subscriber(self, event, callback):
        key = event_to_key(event)
        subscribers = self._subscribers

        if key in subscribers:
            raise Exception('Subscriber already exists.')

        subscribers[key] = callback

    def _remove_subscriber(self, event):
        key = event_to_key(event)
        subscribers = self._subscribers

        if key not in subscribers:
            raise Exception('Unknown subscriber.')

        del subscribers[key]

    def _get_next_command_handle(self):
        if self._pending_commands is None:
            raise Exception('Connection not open.')

        while True:
            handle = self._next_command_handle
            self._next_command_handle = (handle + 1) & 0xFFFFFFFF
            if handle not in self._pending_commands:
                return handle

    def _estimate_next_tx_time(self):
        return self._now()

#TODO handle stack passing
    def send_command(self, command, return_types, callback=None, stack=None) -> Future:
        def executor(resolve, reject):
            handle = self._get_next_command_handle()
            command.handle = handle

            pending_command = PendingCommand(resolve, reject, return_types, command)
            self._pending_commands[handle] = pending_command

            pending_command.last_sent = self._estimate_next_tx_time()
            self.send(command)

        if callback:
            executor(
                lambda result: callback(True, result),
                lambda error: callback(False, error)
            )
        else:
            future = Future()
            executor(future.set_result, future.set_exception)
            return asyncio.wrap_future(future)

    def _remove_pending_command(self, handle):
        pending_command = self._pending_commands.pop(handle, None)
        return pending_command

    def incoming(self, pdus):
        for o in pdus:
            if self._pending_commands is None:
                return

            if isinstance(o, Response):
                pending_command = self._remove_pending_command(o.handle)

                if pending_command is None:
                    if self.is_reliable:
                        self.error(Exception('Unknown handle.'))
                        return
                    else:
                        continue

                pending_command.response(o)
            elif isinstance(o, Notification):
                key = event_to_key(o.event)
                cb = self._subscribers.get(key)

                if cb:
                    cb(o)
            elif isinstance(o, KeepAlive):
                if not (o.time > 0):
                    raise Exception('Bad keepalive timeout.')
            else:
                raise Exception('Unexpected PDU')



