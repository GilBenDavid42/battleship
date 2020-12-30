"""
File: board_settable.py
Purpose: board_settable.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""
import abc


class BytesBoardSettable(abc.ABC):
    @abc.abstractmethod
    def set_on_board(self, bytes_board, board_length):
        pass
