"""
File: placing_inform_parser.py
Purpose: placing_inform_parser.py
Author: Gil Ben David
Change Log: 12/30/2020 
"""
from connection_message.connection_message_container import ConnectionMessageContainer
from connection_message.general_connection_message import GeneralConnectionMessage

PLACING_INFORM_ID = 3


class PlacingInform(ConnectionMessageContainer):
    def __init__(self, placing_hash, general_conn_msg=None):
        if general_conn_msg is None:
            general_conn_msg = GeneralConnectionMessage(PLACING_INFORM_ID)

        self.general_conn_msg = general_conn_msg
        self.placing_hash = placing_hash

    def is_good_message_type(self):
        return self.general_conn_msg.message_type == PLACING_INFORM_ID
