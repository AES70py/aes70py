from ..types.ocastatus import OcaStatus


class RemoteError(Exception):

    def __init__(self, status, cmd):
        self.status = OcaStatus(status)
        self.cmd = cmd

    def __str__(self):
        return (self.status.name)


def check_status(error, status) -> bool:
    return isinstance(error, RemoteError) and error.status == status
