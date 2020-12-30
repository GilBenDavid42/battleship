"""
File: game_server_connection.py
Purpose: game_server_connection.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""
import socket

from game.game_connection import GameConnection


class GameServerConnection(GameConnection):
    def __init__(self, host="", port=8300, connection=None):
        self.port = port
        self.host = host
        self.connection = connection

    def wait_for_another_user(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as listening_socket:
            listening_socket.settimeout(5)
            listening_socket.bind((self.host, self.port))
            listening_socket.listen(1)
            self.connection, addr = listening_socket.accept()

    def wait_for_turn(self):
        data = self.connection.recv(1024)

