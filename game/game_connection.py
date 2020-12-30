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
