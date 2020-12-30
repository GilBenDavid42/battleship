"""
File: bad_position_error.py
Purpose: bad_position_error.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""


class BadPositionError(Exception):
    def __init__(self, position):
        self.position = position

    def __str__(self):
        return f"{self.position} is a bad position."
