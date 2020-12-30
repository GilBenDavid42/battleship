"""
File: game_invite_parser.py
Purpose: game_invite_parser.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""
import struct

from request.connection_message_parser import ConnectionMessageParser
from request.game_invite import GameInvite
from request.general_connection_message_parser import GeneralConnectionMessageParser


class GameInviteParser(ConnectionMessageParser):
    @staticmethod
    def from_stream(stream):
        general_conn_msg = GeneralConnectionMessageParser.from_stream(stream)
        return GameInvite(general_conn_msg)

    @staticmethod
    def to_stream(connection_message):
        return GeneralConnectionMessageParser.from_stream(connection_message.general_conn_msg)
