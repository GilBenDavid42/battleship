"""
File: connection_message_parser.py
Purpose: connection_message_parser.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""

import abc

GAME_INVITE_ID = 1
GAME_ACCEPT_ID = 2
PLACING_INFORM_ID = 3
TURN_ID = 4
TURN_RESULT_ID = 5
PLACEMENT_INFORM_ID = 6


class ConnectionMessageParser(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def from_stream(stream):
        pass

    @staticmethod
    @abc.abstractmethod
    def to_stream(connection_message):
        pass
