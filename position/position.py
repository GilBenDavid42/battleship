"""
File: position2d.py
Purpose: position2d.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""


class Position2D:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos

    def __repr__(self):
        return f"({self.x_pos}, {self.y_pos})"

    def __eq__(self, other):
        return self.x_pos == other.x_pos and self.y_pos == other.y_pos

    def __hash__(self):
        return (str(self.x_pos) + str(self.y_pos)).__hash__()
