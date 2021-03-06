"""
File: general_connection_message_parser.py
Purpose: general_connection_message_parser.py
Author: Gil Ben David
Change Log: 12/30/2020 
"""
import struct

from connection_message.parser.connection_message_parser import ConnectionMessageParser
from connection_message.general_connection_message import GeneralConnectionMessage

GENERAL_CONNECTION_MESSAGE_PACK_FORMAT = "bb"
GENERAL_CONNECTION_MESSAGE_SIZE_BYTES = 2


class GeneralConnectionMessageParser(ConnectionMessageParser):
    @staticmethod
    def from_stream(stream):
        version, message_type = struct.unpack(GENERAL_CONNECTION_MESSAGE_PACK_FORMAT, stream)
        return GeneralConnectionMessage(message_type, version)

    @staticmethod
    def to_stream(connection_message):
        stream = struct.pack(GENERAL_CONNECTION_MESSAGE_PACK_FORMAT, connection_message.version,
                             connection_message.message_type)
        return stream
