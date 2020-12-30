"""
File: main.py
Purpose: main.py
Usage: main.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""

from game.game_board import GameBoard
from game.game_connection import GameLogic
from game.game_manager import GameManager


def main():
    game_board = GameBoard()
    game_logic = GameLogic()
    game_manager = GameManager(game_board, game_logic)


if __name__ == '__main__':
    main()
