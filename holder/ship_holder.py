"""
File: ship_holder.py
Purpose: ship_holder.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""
from holder.board_settable import BytesBoardSettable
from holder.strikable import Strikeable


class ShipHolder(Strikeable, BytesBoardSettable):
    def __init__(self, ship, ship_position, rotation_to_width):
        self.ship = ship
        self.ship_position = ship_position
        self.rotation_to_width = rotation_to_width

    def is_strike(self, position):
        ship_coordinate, coordinate = (self.ship_position.x, position.x) if self.rotation_to_width else (
            self.ship_position.y, position.y)

        return coordinate >= ship_coordinate

    def set_on_board(self, bytes_board, board_length):
        bytes_board_positions = []
        if self.ship.to_width:
            for i in range(self.ship.length):
                bytes_board_positions += [self.ship_position.x_pos + i + self.ship_position.y_pos * board_length]
        else:
            for i in range(self.ship.length):
                bytes_board_positions += [self.ship_position.x_pos + (i + self.ship_position.y_pos) * board_length]

        for bytes_board_pos in bytes_board_positions:
            bytes_board[bytes_board_pos] = self.ship.holder_id
