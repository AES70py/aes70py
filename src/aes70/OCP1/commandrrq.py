from .command import Command

"""
Command packet with response required.
"""
class CommandRrq(Command):
    message_type = 1


