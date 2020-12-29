"""
File: game_object_holder.py
Purpose: game_object_holder.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""
import abc


class GameObjectHolder(abc.ABC):
    def __init__(self, game_object, position):
        
    @abc.abstractmethod
    def can_be_placed(self):