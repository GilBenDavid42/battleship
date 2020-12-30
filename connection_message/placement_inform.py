"""
File: placement_inform.py
Purpose: placement_inform.py
Author: Gil Ben David
Change Log: 12/30/2020 
"""
from connection_message.connection_message_container import ConnectionMessageContainer
from connection_message.general_connection_message import GeneralConnectionMessage

PLACEMENT_INFORM_ID = 6


class PlacementInform(ConnectionMessageContainer):
    def __init__(self, ships_data_bytes, nonce, general_conn_msg=None):
        if general_conn_msg is None:
            general_conn_msg = GeneralConnectionMessage(PLACEMENT_INFORM_ID)
        self.general_conn_msg = general_conn_msg
        self.ships_data_bytes = ships_data_bytes
        self.nonce = nonce

    def is_good_message_type(self):
        return self.general_conn_msg.message_type == PLACEMENT_INFORM_ID
