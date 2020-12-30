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
from connection_message.turn_result import TurnResult

TURN_RESULT_FORMAT = "H"
SHORT_BYTES = 8 * 2


class TurnResultParser(ConnectionMessageParser):
    @staticmethod
    def from_stream(stream):
        general_conn_msg = GeneralConnectionMessageParser.from_stream(stream)
        strike_and_ship = struct.unpack(GENERAL_CONNECTION_MESSAGE_PAD_FORMAT + TURN_RESULT_FORMAT, stream)[0]
        strike = bool(strike_and_ship & 1 << SHORT_BYTES)
        ship = strike_and_ship & (1 << SHORT_BYTES) - 1
        return TurnResult(general_conn_msg, strike, ship)

    @staticmethod
    def to_stream(connection_message):
        stream = GeneralConnectionMessageParser.from_stream(connection_message.general_conn_msg)
        strike_and_ship = connection_message.strike << SHORT_BYTES | connection_message.ship
        stream += struct.pack(TURN_RESULT_FORMAT, strike_and_ship)
        return stream
