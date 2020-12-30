"""
File: game_manager.py
Purpose: game_manager.py
Author: Gil Ben David
Change Log: 12/29/2020 
"""
from position.position import Position
from ship.ship import Ship

FIVE_LENGTH_SHIP_LENGTH = 5
FIVE_LENGTH_SHIP_ID = 1
FOUR_LENGTH_SHIP_LENGTH = 4
FOUR_LENGTH_SHIP_ID = 2
THREE_LENGTH_SHIP_LENGTH = 3
FIRST_THREE_LENGTH_SHIP_ID = 3
SECOND_THREE_LENGTH_SHIP_ID = 4
TWO_LENGTH_SHIP_LENGTH = 2
TWO_LENGTH_SHIP_ID = 5
DEFAULT_SHIPS = [Ship(FIVE_LENGTH_SHIP_LENGTH, FIVE_LENGTH_SHIP_ID),
                 Ship(FOUR_LENGTH_SHIP_LENGTH, FOUR_LENGTH_SHIP_ID),
                 Ship(THREE_LENGTH_SHIP_LENGTH, FIRST_THREE_LENGTH_SHIP_ID),
                 Ship(THREE_LENGTH_SHIP_LENGTH, SECOND_THREE_LENGTH_SHIP_ID),
                 Ship(TWO_LENGTH_SHIP_LENGTH, TWO_LENGTH_SHIP_ID)]


class GameManager:
    def __init__(self, board, game_logic, game_connection, ships=None):
        self.board = board
        self.game_logic = game_logic
        self.game_connection = game_connection
        if ships is None:
            ships = DEFAULT_SHIPS
        self.ships = ships

    @staticmethod
    def _get_position_input():
        pos_input = input(
            "Please choose your x position and you y position separated by space: ")
        x_pos, y_pos = pos_input.split(" ")
        return Position(x_pos, y_pos)

    def _get_ship_inputs(self):
        print(f"Your map is {self.board.side_size}x{self.board.side_size} size")
        for ship in self.ships:
            position_chosen = False
            print(f"You have your ships of length {ship.length} with id {ship.ship_id}")
            while not position_chosen:
                position = self._get_position_input()
                position_chosen = not self.board.is_holder_exists_in(position)
                if position_chosen:
                    self.board.set_ship_holder(position, ship)

    def start_game(self):
        self.game_logic.start_game()
        while not self.game_logic.game_done:
            print("Please give position for your enemy to strike: ")
            enemy_ship_position = self._get_position_input()
            self.game_logic.make_turn(enemy_ship_position)

        if not self.game_logic.is_game_legal():
            print("Game wasn't legal!")
