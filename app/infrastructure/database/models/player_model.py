"""Module app.infrastructure.database.models.player_model"""

from dataclasses import dataclass
from typing import Dict

from app.extension import db


@dataclass
class PlayerModel(db.Model):
    """
    PlayerModel class represents a player in the database.

    Attributes:
        - id (int): The unique identifier of the player.
        - fullname (str): The full name of the player.
        - created_at (datetime): The timestamp of when the player was created.
    """

    __tablename__ = "players"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.now())

    games = db.relationship(
        "GameModel", back_populates="player1", foreign_keys="GameModel.player1_id"
    )
    games_as_player2 = db.relationship(
        "GameModel", back_populates="player2", foreign_keys="GameModel.player2_id"
    )
    games_as_winner = db.relationship(
        "GameModel", back_populates="winner", foreign_keys="GameModel.winner_id"
    )

    def json(self) -> Dict:
        """
        Returns a dictionary representation of the player object.
        """
        return {"id": self.id, "fullname": self.fullname, "created_at": self.created_at}
