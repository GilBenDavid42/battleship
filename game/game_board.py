"""
File: game_board.py
Purpose: game_board.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""
from errors.bad_position_error import BadPositionError


class GameBoard2D:
    def __init__(self, ship_holders=None, board_side_size=10):
        if ship_holders is None:
            ship_holders = {}
        self.ship_holders = ship_holders
        self.board_length = board_side_size

    def get_board_as_bytes(self):
        bytes_board = bytearray([0] * self.board_length * self.board_length)
        for ship_holder in self.ship_holders:
            ship_holder.set_on_board(bytes_board, self.board_length)
        return bytes_board

    def is_holder_exists_in(self, position):
        return position in self.ship_holders

    def _check_position_in_map(self, position):
        too_big_pos = position.x_pos >= self.board_length or position.y_pos >= self.board_length
        too_low_pos = position.x_pos < 0 or position.y_pos < 0
        if too_big_pos or too_low_pos:
            raise BadPositionError(position)

    def get_holder(self, position):
        self._check_position_in_map(position)
        return self.ship_holders[position]

    def set_ship_holder(self, position, ship):
        self.ship_holders[position] = ship

    def get_numeric_position(self, position):
        return position.x_pos + position.y_pos * self.board_length
