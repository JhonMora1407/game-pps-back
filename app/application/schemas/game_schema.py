"""Module app.application.schemas.game_schema"""

from marshmallow import Schema, fields


class GameSchema(Schema):
    """
    Schema for representing a game.

    Attributes:
        - player1_id (int): The ID of player 1. Required field.
        - player2_id (int): The ID of player 2. Required field.
    """

    player1_id = fields.Int(required=True)
    player2_id = fields.Int(required=True)
