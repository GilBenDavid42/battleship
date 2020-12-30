"""
File: game_invite_parser.py
Purpose: game_invite_parser.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""

from connection_message.parser.connection_message_parser import ConnectionMessageParser
from connection_message.game_invite import GameInvite
from connection_message.parser.general_connection_message_parser import GeneralConnectionMessageParser


class GameInviteParser(ConnectionMessageParser):
    @staticmethod
    def from_stream(stream):
        general_conn_msg = GeneralConnectionMessageParser.from_stream(stream)
        return GameInvite(general_conn_msg)

    @staticmethod
    def to_stream(connection_message):
        return GeneralConnectionMessageParser.from_stream(connection_message.general_conn_msg)
