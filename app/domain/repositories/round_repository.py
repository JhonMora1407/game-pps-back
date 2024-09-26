"""Module app.domain.repositories.movement_repository"""

from abc import ABC, abstractmethod

from app.domain.entities.round import Round


class RoundRepository(ABC):
    """Class for MovementRepository interface."""

    @abstractmethod
    def get_by_game_id(self, game_id: int) -> Round | None:
        """
        Abstract method to retrieve a movement by their ID.

        Parameters:
            - movement_id (int): The ID of the movement to retrieve.

        Returns:
            - Movement | None: The movement object if found, None otherwise.
        """
        raise NotImplementedError()

    @abstractmethod
    def create(self, round_game: Round) -> Round:
        """
        Abstract method to save a new movement.

        Parameters:
            - movement (Movement): The movement object to be created.

        Returns:
            - Movement: The created movement object.
        """
        raise NotImplementedError()
