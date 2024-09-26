"""Module app.config"""

import os


class Config:
    """
    Configuration class for the Flask application.

    Attributes:
        - SQLALCHEMY_DATABASE_URI (str): The URI for the database connection.
        - SQLALCHEMY_TRACK_MODIFICATIONS (bool): Flag to enable or disable modification tracking.
    """

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", os.getenv("DOCKER_DATABASE_URL"))
    SQLALCHEMY_TRACK_MODIFICATIONS = False
