"""Module SQLAlchemy repository games.infrastructure.sqlalchemy_game_repository"""

from dataclasses import dataclass

from sqlalchemy.orm import Session

from app.domain.entities.game import Game
from app.domain.repositories.game_repository import GameRepository
from app.infrastructure.database.models.game_model import GameModel


@dataclass
class SQLAlchemyGameRepository(GameRepository):
    """Class for SQLAlchemyGameRepository"""

    db: Session

    def create(self, game: Game) -> GameModel:
        """
        Creates a new game in the repository.

        Args:
            - game (Game): The game object to be created.

        Returns:
            - Game: The created game object.
        """
        game_model = GameModel(**game)
        self.db.session.add(game_model)
        self.db.session.commit()

        return game_model

    def get_by_id(self, game_id: int) -> GameModel:
        """
        Gets a game by its id.

        Args:
            - game_id (int): The game's id.

        Returns:
            - Game: The game object.
        """
        return self.db.session.query(GameModel).get(game_id)
