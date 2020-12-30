"""
File: game_logic.py
Purpose: game_logic.py
Author: Gil Ben David
Change Log: 12/30/2020 
"""
import abc

GAME_VERSION = 1


class GameLogic(abc.ABC):
    @abc.abstractmethod
    def start_game(self):
        pass

    @abc.abstractmethod
    def make_turn(self, enemy_ship_position):
        pass
