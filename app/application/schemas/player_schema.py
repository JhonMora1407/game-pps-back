"""Module app.application.schemas.player_schema"""

from marshmallow import Schema, fields


class PlayerSchema(Schema):
    """
    Schema for representing a player.

    Attributes:
        fullname (str): The full name of the player. Required field.
    """

    fullname = fields.Str(required=True)
