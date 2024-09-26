"""Module app.domain.models.game"""

from dataclasses import dataclass
from datetime import datetime
from typing import Dict

from app.extension import db

PLAYERS_ID = "players.id"


@dataclass
class GameModel(db.Model):
    """
    Game class represents a game between two players.

    Attributes:
        - id (int): The unique identifier of the game.
        - player_one_id (int): The ID of the first player.
        - player_two_id (int): The ID of the second player.
        - status (str): The status of the game (ongoing or finished).
        - winner_id (int): The ID of the winner player.
        - created_at (datetime): The datetime when the game was created.
        - updated_at (datetime): The datetime when the game was last updated.

    Relationships:
        - player_one (Player): The relationship to the first player.
        - player_two (Player): The relationship to the second player.
        - winner (Player): The relationship to the winner player.
    """

    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    player1_id = db.Column(db.Integer, db.ForeignKey(PLAYERS_ID), nullable=False)
    player2_id = db.Column(db.Integer, db.ForeignKey(PLAYERS_ID), nullable=False)
    status = db.Column(
        db.Enum("ongoing", "finished", name="status"), nullable=False, default="ongoing"
    )
    winner_id = db.Column(db.Integer, db.ForeignKey(PLAYERS_ID), nullable=True)
    current_round = db.Column(db.Integer, default=0)
    round_winned_player1 = db.Column(db.Integer, default=0)
    round_winned_player2 = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    player1 = db.relationship("PlayerModel", foreign_keys=[player1_id], back_populates="games")
    player2 = db.relationship("PlayerModel", foreign_keys=[player2_id], back_populates="games")
    winner = db.relationship("PlayerModel", foreign_keys=[winner_id], back_populates="games")
    rounds = db.relationship(
        "RoundModel", back_populates="games", foreign_keys="RoundModel.game_id"
    )

    def json(self) -> Dict:
        """
        Returns a dictionary representation of the game object.

        Parameters:
            None

        Returns:
            Dict: A dictionary representation of the game object.
        """
        return {
            "id": self.id,
            "player1_id": self.player1_id,
            "player2_id": self.player2_id,
            "current_round": self.current_round,
            "round_winned_player1": self.round_winned_player1,
            "round_winned_player2": self.round_winned_player2,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "updated_at": self.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
            "winner": self.winner.json() if self.winner else None,
        }

    def increment_round(self) -> None:
        """
        Increments the round of the game by 1.

        Parameters:
            None

        Returns:
            None
        """
        self.current_round += 1

    def increment_round_winned_player1(self) -> None:
        """
        Increments the round winned by player one of the game by 1.

        Parameters:
            None

        Returns:
            None
        """
        self.round_winned_player1 += 1

    def increment_round_winned_player2(self) -> None:
        """
        Increments the round winned by player two of the game by 1.

        Parameters:
            None

        Returns:
            None
        """
        self.round_winned_player2 += 1
