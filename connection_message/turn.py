"""
File: turn.py
Purpose: turn.py
Author: Gil Ben David
Change Log: 12/30/2020 
"""
from connection_message.connection_message_container import ConnectionMessageContainer
from connection_message.general_connection_message import GeneralConnectionMessage

TURN_ID = 4


class Turn(ConnectionMessageContainer):
    def __init__(self, position, general_conn_msg=None):
        if general_conn_msg is None:
            general_conn_msg = GeneralConnectionMessage(TURN_ID)

        self.general_conn_msg = general_conn_msg
        self.position = position

    def is_good_message_type(self):
        return self.general_conn_msg.message_type == TURN_ID
