"""Module app.domain.services.player_service"""

from dataclasses import dataclass
from typing import Dict

from app.domain.entities.player import Player
from app.domain.exceptions.player_not_found_exception import PlayerNotFoundException
from app.domain.repositories.player_repository import PlayerRepository


@dataclass
class PlayerService:
    """
    PlayerService class responsible for managing player-related operations.

    Attributes:
        - player_repository (PlayerRepository): The repository for accessing player data.

    Methods:
        - get_by_id(player_id: int) -> Player:
            Retrieves a player by their ID.

        - create(data: Dict) -> Player:
            Creates a new player using the provided data.

    Raises:
        - PlayerNotFoundException: If a player with the given ID does not exist.
    """

    player_repository: PlayerRepository

    def get_by_id(self, player_id: int) -> Player:
        """
        Retrieves a player by their ID.

        Args:
            - player_id (int): The ID of the player to retrieve.

        Returns:
            - Player: The player object.

        Raises:
            - PlayerNotFoundException: If no player is found with the given ID.
        """

        player_repository = self.player_repository.get_by_id(player_id)

        if player_repository is None:
            raise PlayerNotFoundException(player_id=player_id)

        return player_repository

    def create(self, data: Dict) -> Player:
        """
        Creates a new player.

        Args:
            - data (Dict): A dictionary containing the player data.

        Returns:
            - Player: The created player object.
        """
        return self.player_repository.create(data)
