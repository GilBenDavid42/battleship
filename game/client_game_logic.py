"""
File: client_game_logic.py
Purpose: client_game_logic.py
Author: Gil Ben David
Change Log: 12/30/2020 
"""
import hashlib

from connection_message.connection_message_container import ConnectionMessageContainer
from connection_message.game_invite import GameInvite
from connection_message.parser.game_accept_parser import GameAcceptParser
from connection_message.parser.game_invite_parser import GameInviteParser
from connection_message.parser.general_connection_message_parser import GeneralConnectionMessageParser
from connection_message.parser.placement_inform_parser import PlacementInformParser
from connection_message.parser.turn_parser import TurnParser
from connection_message.parser.turn_result_parser import TurnResultParser
from connection_message.placement_inform import PLACEMENT_INFORM_ID, PlacementInform
from connection_message.placing_inform import PlacingInform
from connection_message.turn import Turn
from connection_message.turn_result import TURN_RESULT_ID, TurnResult
from errors.bad_connection_message_type_error import BadConnectionMessageTypeError
from game.game_logic import GameLogic

MAX_BUFFER_SIZE = 4096


class ClientGameLogic(GameLogic):
    def __init__(self, game_connection, game_board):
        self.game_connection = game_connection
        self.game_board = game_board
        self.game_done = False
        self.enemy_placing_inform = None

    def get_board_hash(self):
        return hashlib.sha256(self.game_board.get_board_as_bytes())

    def finish_game(self):
        self.game_done = True

    def turn_result_treat(self, turn_result, enemy_ship_position):
        if turn_result.strike:
            self.make_turn()

    def start_game(self):
        self.game_connection.connection.sendall(GameInviteParser.to_stream(GameInvite()))
        game_accept = GameAcceptParser.from_stream(self.game_connection.connection.recv(MAX_BUFFER_SIZE))
        ConnectionMessageContainer.check_connection_message(game_accept)
        self.game_connection.connection.sendall(GameInviteParser.to_stream(GameInvite()))
        game_accept = GameAcceptParser.from_stream(self.game_connection.connection.recv(MAX_BUFFER_SIZE))
        ConnectionMessageContainer.check_connection_message(game_accept)

        self.enemy_placing_inform = PlacingInform(self.get_board_hash())

    def make_turn(self, enemy_ship_position):

        numeric_pos = self.game_board.get_numeric_position(enemy_ship_position)

        turn_stream = TurnParser.to_stream(Turn(numeric_pos))
        self.game_connection.connection.sendall(turn_stream)
        message_stream = self.game_connection.connection.recv(MAX_BUFFER_SIZE)
        general_conn_msg = GeneralConnectionMessageParser.from_stream(message_stream)
        general_conn_msg.check_message_version()
        if general_conn_msg.message_type == TURN_RESULT_ID:
            turn_result = TurnResultParser.from_stream(message_stream)
            self.turn_result_treat(turn_result)
        elif general_conn_msg.message_type == PLACEMENT_INFORM_ID:
            placement_inform = PlacementInformParser.from_stream(message_stream)
        else:
            raise BadConnectionMessageTypeError()
