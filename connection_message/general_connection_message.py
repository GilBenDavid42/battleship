"""
File: general_connection_message.py
Purpose: general_connection_message.py
Author: Gil Ben David
Change Log: 12/30/2020 
"""
from errors.bad_connection_message_version_error import BadConnectionMessageVersionError

CURRENT_VERSION = 1


class GeneralConnectionMessage:
    def __init__(self, message_type, version=CURRENT_VERSION):
        self.version = version
        self.message_type = message_type

    def check_message_version(self, version=CURRENT_VERSION):
        if self.version == version:
            raise BadConnectionMessageVersionError()
