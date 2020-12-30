"""
File: placement_inform.py
Purpose: placement_inform.py
Author: Gil Ben David
Change Log: 12/30/2020 
"""


class PlacementInform:
    def __init__(self, general_conn_msg, placing_hash, ships_data_bytes, nonce):
        self.general_conn_msg = general_conn_msg
        self.placing_hash = placing_hash
        self.ships_data_bytes = ships_data_bytes
        self.nonce = nonce
