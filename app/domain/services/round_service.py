"""Module app.domain.services.round_service"""

from dataclasses import dataclass
from typing import List

from app.domain.entities.round import Round
from app.domain.exceptions.round_not_found_exception import RoundNotFoundException
from app.domain.repositories.round_repository import RoundRepository


@dataclass
class RoundService:

    round_repository: RoundRepository

    def get_by_game_id(self, game_id: int) -> List[Round]:
        round_repository = self.round_repository.get_by_game_id(game_id)

        if round_repository is None:
            raise RoundNotFoundException(game_id=game_id)

        return [rounds.json() for rounds in round_repository]

    def create(self, data: Round) -> Round:
        """
        Creates a new game.

        Args:
            - data (Dict): A dictionary containing the data for the new game.

        Returns:
            - Game: The newly created game object.
        """
        return self.round_repository.create(data)
