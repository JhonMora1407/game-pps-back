"""Module app.init"""

from dotenv import load_dotenv
from flask import Flask

from app.application.controllers.game_controller import game_blueprint
from app.application.controllers.player_controller import player_blueprint
from app.application.controllers.round_controller import round_blueprint
from app.extension import db

from .config import Config


def create_app():
    """
    Creates and configures the Flask application.

    Returns:
        - Flask: The configured Flask application.
    """
    load_dotenv()

    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(player_blueprint)
    app.register_blueprint(game_blueprint)
    app.register_blueprint(round_blueprint)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
