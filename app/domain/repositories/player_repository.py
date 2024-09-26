"""Module app.domain.repositories.player_repository"""

from abc import ABC, abstractmethod

from app.domain.entities.player import Player


class PlayerRepository(ABC):
    """Class for PlayerRepository interface."""

    @abstractmethod
    def get_by_id(self, player_id: int) -> Player | None:
        """
        Abstract method to retrieve a player by their ID.

        Parameters:
            - player_id (int): The ID of the player to retrieve.

        Returns:
            - Player | None: The player object if found, None otherwise.
        """
        raise NotImplementedError()

    @abstractmethod
    def create(self, player: Player) -> Player:
        """
        Abstract method to create a new player.

        Parameters:
            - player (Player): The player object to be created.

        Returns:
            - Player: The created player object.
        """
        raise NotImplementedError()
