"""
File: placing_inform_parser.py
Purpose: placing_inform_parser.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""
import struct

from connection_message.parser.connection_message_parser import ConnectionMessageParser
from connection_message.parser.general_connection_message_parser import GeneralConnectionMessageParser, \
    GENERAL_CONNECTION_MESSAGE_PAD_FORMAT
from connection_message.placing_inform import PlacingInform

PLACING_INFORM_FORMAT = "s"


class PlacingInformParser(ConnectionMessageParser):

    @staticmethod
    def from_stream(stream):
        general_conn_msg = GeneralConnectionMessageParser.from_stream(stream)
        placing_hash = struct.unpack(GENERAL_CONNECTION_MESSAGE_PAD_FORMAT + PLACING_INFORM_FORMAT, stream)

        return PlacingInform(general_conn_msg, placing_hash)

    @staticmethod
    def to_stream(connection_message):
        stream = GeneralConnectionMessageParser.from_stream(connection_message.general_conn_msg)
        stream += struct.pack(PLACING_INFORM_FORMAT, connection_message.placing_hash)
        return stream
