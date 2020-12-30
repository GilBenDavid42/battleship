"""
File: bad_connection_message_version_error.py
Purpose: bad_connection_message_version_error.py
Author: Gil Ben David
Change Log: 12/30/2020 
"""
from errors.bad_connection_message_error import BadConnectionMessageError


class BadConnectionMessageVersionError(BadConnectionMessageError):
    def __init__(self):
        super(BadConnectionMessageVersionError, self).__init__("version")
