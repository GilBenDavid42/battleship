"""
File: bad_position_error.py
Purpose: bad_position_error.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""
import abc


class Error(Exception):
    def __str__(self):
        