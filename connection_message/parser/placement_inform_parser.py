"""
File: placement_inform_parser.py
Purpose: placement_inform_parser.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""
import struct

from connection_message.parser.connection_message_parser import ConnectionMessageParser
from connection_message.parser.general_connection_message_parser import GeneralConnectionMessageParser, \
    GENERAL_CONNECTION_MESSAGE_SIZE_BYTES
from connection_message.placement_inform import PlacementInform

PLACING_INFORM_FORMAT = "I"
INTEGER_SIZE = 4


class PlacementInformParser(ConnectionMessageParser):
    @staticmethod
    def from_stream(stream):
        general_conn_msg = GeneralConnectionMessageParser.from_stream(stream)
        stream = stream[GENERAL_CONNECTION_MESSAGE_SIZE_BYTES:]
        ships_data_bytes = stream[:-INTEGER_SIZE]
        nonce = struct.unpack(PLACING_INFORM_FORMAT, stream[-INTEGER_SIZE:])

        return PlacementInform(ships_data_bytes, nonce, general_conn_msg)

    @staticmethod
    def to_stream(connection_message):
        stream = GeneralConnectionMessageParser.from_stream(connection_message.general_conn_msg)
        stream += connection_message.ships_data_bytes + struct.pack(PLACING_INFORM_FORMAT, connection_message.nonce)
        return stream

