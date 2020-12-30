"""
File: strikable.py
Purpose: strikable.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""
import abc


class Strikeable(abc.ABC):
    @abc.abstractmethod
    def is_strike(self, position):
        pass
