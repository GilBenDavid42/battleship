"""
File: game_accept.py
Purpose: game_accept.py
Author: Gil Ben David
Change Log: 12/30/2020 
"""
from connection_message.connection_message_container import ConnectionMessageContainer
from connection_message.general_connection_message import GeneralConnectionMessage

GAME_ACCEPT_ID = 2


class GameAccept(ConnectionMessageContainer):
    def __init__(self, general_conn_msg=None):
        if general_conn_msg is None:
            general_conn_msg = GeneralConnectionMessage(GAME_ACCEPT_ID)

        self.general_conn_msg = general_conn_msg

    def is_good_message_type(self):
        return self.general_conn_msg.message_type == GAME_ACCEPT_ID
