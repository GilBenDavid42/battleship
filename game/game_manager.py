"""
File: game_manager.py
Purpose: game_manager.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""
from game.ship import Ship


class GameManager:
    def __init__(self, board, game_logic, ships=None):
        self.game_board = board
        self.game_logic = game_logic
        if ships is None:
            ships = b''
        self.ships = ships

    def start_game(self):
        for ship in self.ships:
            ship

        self.game_logic.start_game()
        self.game_logic.make_turn()
