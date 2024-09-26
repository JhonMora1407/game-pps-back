"""Module app.utils.exceptions.init"""

from typing import Tuple

from flask import jsonify
from marshmallow import ValidationError
from sqlalchemy.exc import SQLAlchemyError

from app.domain.exceptions.game_not_found_exception import GameNotFoundException
from app.domain.exceptions.game_over_exception import GameOverException
from app.domain.exceptions.move_invalid_exception import MoveInvalidException
from app.domain.exceptions.player_not_found_exception import PlayerNotFoundException

BAD_REQUEST = "Bad request"


def handle_exception(err) -> Tuple:
    """
    Handle an exception by calling two exception handlers: game_exception and general_exception.

    Args:
        - e: The exception object to be handled.

    Returns:
        - None
    """
    if isinstance(err, ValidationError):
        new_message = dict(err.messages.items())
        response = {"error": BAD_REQUEST, "code": "400", "message": new_message}
        return jsonify(response), 400

    if isinstance(err, GameNotFoundException):
        response = {"error": "Not found", "code": "404", "message": str(err)}
        return jsonify(response), 404

    if isinstance(err, MoveInvalidException):
        response = {"error": BAD_REQUEST, "code": "400", "message": str(err)}
        return jsonify(response), 400

    if isinstance(err, PlayerNotFoundException):
        response = {"error": "Not found", "code": "404", "message": str(err)}
        return jsonify(response), 404

    if isinstance(err, GameOverException):
        response = {"error": BAD_REQUEST, "code": "400", "message": str(err)}
        return jsonify(response), 400

    if isinstance(err, SQLAlchemyError):
        response = {"error": "Database error", "code": "500", "message": str(err)}
        return jsonify(response), 500

    response = {"error": "Internal server error", "code": "500", "message": str(err)}
    return jsonify(response), 500
