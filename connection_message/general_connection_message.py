"""
File: general_connection_message.py
Purpose: general_connection_message.py
Author: Gil Ben David
Change Log: 12/30/2020 
"""


class GeneralConnectionMessage:
    def __init__(self, version, message_type):
        self.version = version
        self.message_type = message_type
