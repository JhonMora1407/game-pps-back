"""Module repository SQLAlchemy rounds.infrastructure.sqlalchemy_round_repository"""

from dataclasses import dataclass

from sqlalchemy.orm import Session

from app.domain.entities.round import Round
from app.domain.repositories.round_repository import RoundRepository
from app.infrastructure.database.models.round_model import RoundModel


@dataclass
class SQLAlchemyRoundRepository(RoundRepository):
    """Class for SQLAlchemyRoundRepository"""

    db: Session

    def create(self, round_game: Round) -> Round:
        """
        Saves a new round in the repository.

        Args:
            - round (Round): The round object to be saved.

        Returns:
            - Round: The saved round object.
        """
        round_model = RoundModel(**round_game)
        self.db.session.add(round_model)
        self.db.session.commit()

        return round

    def get_by_game_id(self, game_id: int) -> Round:
        """
        Gets a round by its id.

        Args:
            - round_id (int): The round's id.

        Returns:
            - Round: The round object.
        """
        return self.db.session.query(RoundModel).filter_by(game_id=game_id).all()
