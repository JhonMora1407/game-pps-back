"""Module app.application.controllers.movement_controller"""

from typing import Tuple

from flask import blueprints, jsonify, request

from app.domain.services.round_service import RoundService
from app.extension import db
from app.infrastructure.repositories.sqlalchemy_round_repository import (
    SQLAlchemyRoundRepository,
)
from app.utils.decorators import handle_exceptions

round_blueprint = blueprints.Blueprint("round", __name__)


@round_blueprint.route("/rounds", methods=["GET"])
@handle_exceptions
def get_by_game_id() -> Tuple:
    """
    Get rounds by game ID.

    Returns:
        - Tuple: A tuple containing the JSON response and the HTTP status code 200.
    """
    game_id = request.args.get("game_id")
    sql_round_repository = SQLAlchemyRoundRepository(db)

    result = RoundService(sql_round_repository).get_by_game_id(game_id)

    return jsonify(result), 200
