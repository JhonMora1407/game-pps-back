"""Module app.domain.models.round_model"""

from dataclasses import dataclass
from datetime import datetime
from typing import Dict

from app.extension import db


# @dataclass
class RoundModel(db.Model):

    __tablename__ = "rounds"

    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey("games.id"), nullable=False)
    player1_move = db.Column(db.Enum("rock", "paper", "scissors", name="move"), nullable=False)
    player2_move = db.Column(db.Enum("rock", "paper", "scissors", name="move"), nullable=False)
    round_game = db.Column(db.Integer, nullable=False, default=0)
    winner = db.Column(db.Enum("player1", "player2", "draw", name="winner"), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    games = db.relationship("GameModel", foreign_keys=[game_id], back_populates="rounds")

    def json(self) -> Dict:
        """
        Returns a dictionary representation of the round object.
        """
        return {
            "id": self.id,
            "game_id": self.game_id,
            "player1_move": self.player1_move,
            "player2_move": self.player2_move,
            "round_game": self.round_game,
            "winner": self.winner,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
        }
