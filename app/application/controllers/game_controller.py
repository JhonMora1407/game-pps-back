"""Module app.infrastructure.controllers.game_controller"""

from typing import Tuple

from flask import blueprints, jsonify, request

from app.application.schemas.game_schema import GameSchema
from app.application.schemas.round_schema import RoundSchema
from app.domain.services.game_service import GameService
from app.extension import db
from app.infrastructure.repositories.sqlalchemy_game_repository import (
    SQLAlchemyGameRepository,
)
from app.infrastructure.repositories.sqlalchemy_player_repository import (
    SQLAlchemyPlayerRepository,
)
from app.infrastructure.repositories.sqlalchemy_round_repository import (
    SQLAlchemyRoundRepository,
)
from app.utils.decorators import handle_exceptions

game_blueprint = blueprints.Blueprint("game", __name__)
round_schema = RoundSchema()
game_schema = GameSchema()


@game_blueprint.route("/games/<game_id>", methods=["GET"])
@handle_exceptions
def get_game(game_id: int) -> Tuple:
    """
    Get a game by its ID.

    Args:
        - game_id: The ID of the game to retrieve.

    Returns:
        - Tuple: A tuple containing the JSON representation of the game and the HTTP status code
          200.
    """
    sql_game_repository = SQLAlchemyGameRepository(db)

    result = GameService(sql_game_repository).get_by_id(game_id)

    return jsonify(result.json()), 200


@game_blueprint.route("/games", methods=["POST"])
@handle_exceptions
def create_game() -> Tuple:
    """
    Create a new game.

    Returns:
        - Tuple: A tuple containing the JSON representation of the created game and the HTTP status
          code 201.
    """
    validated_data = game_schema.load(request.json)
    sql_game_repository = SQLAlchemyGameRepository(db)
    sql_player_repository = SQLAlchemyPlayerRepository(db)

    result = GameService(sql_game_repository, player_repository=sql_player_repository).create(
        validated_data
    )

    return jsonify(result.json()), 201


@game_blueprint.route("/games/<game_id>/play", methods=["POST"])
@handle_exceptions
def play_game(game_id: int) -> Tuple:
    """
    Play a round of the game.

    Args:
        - game_id: The ID of the game to play.

    Returns:
        - Tuple: A tuple containing the JSON representation of the updated game and the HTTP status
          code 200.
    """
    validated_data = round_schema.load(request.json)
    sql_game_repository = SQLAlchemyGameRepository(db)
    sql_round_repository = SQLAlchemyRoundRepository(db)

    result = GameService(sql_game_repository, sql_round_repository).play_round(
        game_id=game_id, **validated_data
    )

    return jsonify(result.json()), 200
