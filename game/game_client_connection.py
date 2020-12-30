"""
File: game_client_connection.py
Purpose: game_client_connection.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""
import socket

from game.game_connection import GameConnection
from game.game_server_connection import INFINITE_TIMEOUT


class GameClientConnection(GameConnection):
    def __init__(self, host="127.0.0.1", port=8300, timeout=INFINITE_TIMEOUT, connection=None):
        self.port = port
        self.host = host
        self.timeout = timeout
        self.connection = connection

    def wait_for_another_user(self):
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connection.connect((self.host, self.port))

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()


