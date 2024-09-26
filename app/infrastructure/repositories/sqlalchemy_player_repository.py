"""Module SQLAlchemy repository players.infrastructure.sqlalchemy_players_repository"""

from dataclasses import dataclass

from sqlalchemy.orm import Session

from app.domain.entities.player import Player
from app.domain.repositories.player_repository import PlayerRepository
from app.infrastructure.database.models.player_model import PlayerModel


@dataclass
class SQLAlchemyPlayerRepository(PlayerRepository):
    """Class for SQLAlchemyPlayersRepository"""

    db: Session

    def create(self, player: Player) -> Player:
        """
        Creates a new player in the repository.

        Args:
            - player (Player): The player object to be created.

        Returns:
            - Player: The created player object.
        """
        player_model = PlayerModel(**player)
        self.db.session.add(player_model)
        self.db.session.commit()

        return player_model

    def get_by_id(self, player_id: int) -> Player:
        """
        Gets a player by its id.

        Args:
            - player_id (int): The player's id.

        Returns:
            - Player: The player object.
        """
        return self.db.session.query(PlayerModel).get(player_id)
