"""
File: bad_connection_message_type_error.py
Purpose: bad_connection_message_type_error.py
Author: Gil Ben David
Change Log: 12/30/2020 
"""
from errors.bad_connection_message_error import BadConnectionMessageError


class BadConnectionMessageTypeError(BadConnectionMessageError):
    def __init__(self):
        super(BadConnectionMessageTypeError, self).__init__("type")

