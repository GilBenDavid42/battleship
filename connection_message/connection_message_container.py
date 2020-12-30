"""
File: connection_message_container.py
Purpose: connection_message_container.py
Author: Gil Ben David
Change Log: 12/30/2020 
"""
import abc

from errors.bad_connection_message_type_error import BadConnectionMessageTypeError
from errors.bad_connection_message_version_error import BadConnectionMessageVersionError


class ConnectionMessageContainer(abc.ABC):
    @abc.abstractmethod
    def is_good_message_type(self):
        pass

    @staticmethod
    def check_connection_message_type(connection_message):
        if not connection_message.is_good_message_type():
            raise BadConnectionMessageTypeError()

    @staticmethod
    def check_connection_message(connection_message):
        connection_message.general_conn_msg.check_message_version()
        ConnectionMessageContainer.check_connection_message_type(connection_message)
