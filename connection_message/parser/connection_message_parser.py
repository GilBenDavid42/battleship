"""
File: connection_message_parser.py
Purpose: connection_message_parser.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""

import abc




class ConnectionMessageParser(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def from_stream(stream):
        pass

    @staticmethod
    @abc.abstractmethod
    def to_stream(connection_message):
        pass
