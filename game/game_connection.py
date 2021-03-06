"""
File: game_connection.py
Purpose: game_connection.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""
import abc


class GameConnection(abc.ABC):
    @abc.abstractmethod
    def wait_for_another_user(self):
        pass

    @abc.abstractmethod
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
