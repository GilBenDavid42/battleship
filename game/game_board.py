"""
File: game_board.py
Purpose: game_board.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""


class GameBoard:
    def __init__(self, board_side_size=10, bytes_board=None):
        if bytes_board is None:
            bytes_board = bytearray([0] * board_side_size * board_side_size)
        self.bytes_board = bytes_board
        self.board_side_size = board_side_size

    def get_(self, column, row):
        return self.bytes_board[column + (10 * row)]
