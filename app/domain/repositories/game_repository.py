"""Module app.domain.repository.game_repository"""

from abc import ABC, abstractmethod

from app.domain.entities.game import Game


class GameRepository(ABC):
    """Class for GameRepository interface."""

    @abstractmethod
    def get_by_id(self, game_id: int) -> Game | None:
        """
        Abstract method to retrieve a game by their ID.

        Parameters:
            - game_id (int): The ID of the game to retrieve.

        Returns:
            - Game | None: The game object if found, None otherwise.
        """
        raise NotImplementedError()

    @abstractmethod
    def create(self, game: Game) -> Game:
        """
        Abstract method to create a new game.

        Parameters:
            - game (Game): The game object to be created.

        Returns:
            - Game: The created game object.
        """
        raise NotImplementedError()
