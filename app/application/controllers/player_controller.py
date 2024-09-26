"""Module app.application.controllers.player_controller"""

from typing import Tuple

from flask import blueprints, jsonify, request

from app.application.schemas.player_schema import PlayerSchema
from app.domain.services.player_service import PlayerService
from app.extension import db
from app.infrastructure.repositories.sqlalchemy_player_repository import (
    SQLAlchemyPlayerRepository,
)
from app.utils.decorators import handle_exceptions

player_blueprint = blueprints.Blueprint("player", __name__)
player_schema = PlayerSchema()


@player_blueprint.route("/players/<player_id>", methods=["GET"])
@handle_exceptions
def get_player_by_id(player_id: int) -> Tuple:
    """
    Get a player by its ID.

    Args:
        - player_id: The ID of the player to retrieve.

    Returns:
        - Tuple: A tuple containing the JSON representation of the player and the HTTP status code
          200.
    """

    sql_player_repository = SQLAlchemyPlayerRepository(db)

    result = PlayerService(sql_player_repository).get_by_id(player_id)

    return jsonify(result.json()), 200


@player_blueprint.route("/players", methods=["POST"])
@handle_exceptions
def create_player() -> Tuple:
    """
    Create a new player.

    Returns:
        - Tuple: A tuple containing the JSON representation of the created player and the HTTP
          status code 201.
    """
    validated_data = player_schema.load(request.json)
    sql_player_repository = SQLAlchemyPlayerRepository(db)

    result = PlayerService(sql_player_repository).create(validated_data)

    return jsonify(result.json()), 201
