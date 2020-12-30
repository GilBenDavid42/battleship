"""
File: bad_connection_message_error.py
Purpose: bad_connection_message_error.py
Author: Gil Ben David
Change Log: 12/30/2020 
"""


class BadConnectionMessageError(Exception):
    def __init__(self, bad_message_attr):
        self.bad_message_attr = bad_message_attr

    def __str__(self):
        return f"Got bad connection message {self.bad_message_attr}"
