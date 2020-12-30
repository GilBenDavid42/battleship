"""
File: game_server_connection.py
Purpose: game_server_connection.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""
import socket

from game.game_connection import GameConnection

INFINITE_TIMEOUT = None


class GameServerConnection(GameConnection):
    def __init__(self, host="", port=8300, connection=None, listening_socket=None, timeout=INFINITE_TIMEOUT):
        self.port = port
        self.host = host
        self.connection = connection
        self.listening_socket = listening_socket
        self.timeout = timeout

    def wait_for_another_user(self):
        self.listening_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listening_socket.settimeout(self.timeout)
        self.listening_socket.bind((self.host, self.port))
        self.listening_socket.listen(1)
        self.connection, addr = self.listening_socket.accept()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.listening_socket.close()
        self.connection.close()
