"""Module app.application.schemas.round_schema"""

from marshmallow import Schema, ValidationError, fields, validates

from app.domain.exceptions.move_invalid_exception import MoveInvalidException

VALID_MOVES = ["rock", "paper", "scissors"]


class RoundSchema(Schema):
    """
    Schema for representing a round in a game.

    Attributes:
        - player1_move (str): The move made by player 1. Must be one of "rock", "paper", or
          "scissors".
        - player2_move (str): The move made by player 2. Must be one of "rock", "paper", or
          "scissors".
    """

    player1_move = fields.Str(required=True)
    player2_move = fields.Str(required=True)

    @validates("player1_move")
    def validate_player1_move(self, value: str) -> ValidationError:
        """
        Validate the value of player1_move.

        Parameters:
            - value (str): The value of player1_move to be validated.

        Raises:
            - ValidationError: If the value is not in the list of valid moves.
        """
        if value not in VALID_MOVES:
            raise MoveInvalidException(VALID_MOVES)

    @validates("player2_move")
    def validate_player2_move(self, value: str) -> ValidationError:
        """
        Validate the value of player2_move.

        Parameters:
            - value (str): The value of player2_move to be validated.

        Raises:
            - ValidationError: If the value is not in the list of valid moves.
        """
        if value not in VALID_MOVES:
            raise MoveInvalidException(VALID_MOVES)
