"""
File: turn_parser.py
Purpose: turn_parser.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""
import struct

from connection_message.parser.connection_message_parser import ConnectionMessageParser
from connection_message.parser.general_connection_message_parser import GeneralConnectionMessageParser, \
    GENERAL_CONNECTION_MESSAGE_PAD_FORMAT
from connection_message.turn import Turn

TURN_FORMAT = "b"


class TurnParser(ConnectionMessageParser):

    @staticmethod
    def from_stream(stream):
        general_conn_msg = GeneralConnectionMessageParser.from_stream(stream)
        position = struct.unpack(GENERAL_CONNECTION_MESSAGE_PAD_FORMAT + TURN_FORMAT, stream)

        return Turn(general_conn_msg, position)

    @staticmethod
    def to_stream(connection_message):
        stream = GeneralConnectionMessageParser.from_stream(connection_message.general_conn_msg)
        stream += struct.pack(TURN_FORMAT, connection_message.position)
        return stream
