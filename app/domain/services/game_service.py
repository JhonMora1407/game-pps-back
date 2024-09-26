"""Module app.domain.service.game_service"""

from dataclasses import dataclass
from typing import Dict, Optional

from app.domain.entities.game import Game
from app.domain.exceptions.game_not_found_exception import GameNotFoundException
from app.domain.exceptions.game_over_exception import GameOverException
from app.domain.exceptions.player_not_found_exception import PlayerNotFoundException
from app.domain.repositories.game_repository import GameRepository
from app.domain.repositories.player_repository import PlayerRepository
from app.domain.repositories.round_repository import RoundRepository
from app.domain.services.player_service import PlayerService
from app.domain.services.round_service import RoundService

rules = {"rock": "scissors", "paper": "rock", "scissors": "paper"}


@dataclass
class GameService:
    """GameService class provides game-related services."""

    game_repository: GameRepository
    round_repository: Optional[RoundRepository] = None
    player_repository: Optional[PlayerRepository] = None

    def get_by_id(self, game_id: int) -> Game:
        """
        Retrieves a game by its ID.

        Args:
            - game_id (int): The ID of the game to retrieve.

        Returns:
            - Game: The game object.

        Raises:
            - GameNotFoundException: If the game with the specified ID is not found.
        """
        game_repository = self.game_repository.get_by_id(game_id)

        if game_repository is None:
            raise GameNotFoundException(game_id=game_id)

        return game_repository

    def create(self, data: Dict) -> Game:
        """
        Creates a new game.

        Args:
            - data (Dict): A dictionary containing the data for the new game.

        Returns:
            - Game: The newly created game object.
        """
        player_service = PlayerService(self.player_repository)

        for player_id in data.values():
            player_service.get_by_id(player_id)

        return self.game_repository.create(data)

    def play_round(self, game_id: int, player1_move: str, player2_move: str) -> Game:
        """
        Plays a round of the game.

        Args:
            - game_id (int): The ID of the game.
            - player1_move (str): The move made by player 1.
            - player2_move (str): The move made by player 2.

        Returns:
            - Game: The updated game object after playing the round.
        """
        game = self.get_by_id(game_id)
        game.increment_round()

        if game.winner:
            raise GameOverException(game.winner.fullname)

        round_winner = self.determine_round_winner(player1_move, player2_move, game)
        game.winner_id = self.determine_game_winner(game)

        self.create_round(game_id, player1_move, player2_move, round_winner, game.current_round)

        return game

    def create_round(
        self, game_id: int, player1_move: str, player2_move: str, round_winner: str, round_game: int
    ) -> None:
        """
        Creates a new round for the game.

        Args:
            - game_id (int): The ID of the game.
            - player1_move (str): The move made by player 1.
            - player2_move (str): The move made by player 2.
            - round_winner (str): The winner of the round.
            - round_game (int): The current round of the game.
        """
        data_round = {
            "game_id": game_id,
            "player1_move": player1_move,
            "player2_move": player2_move,
            "winner": round_winner,
            "round_game": round_game,
        }

        RoundService(self.round_repository).create(data_round)

    @staticmethod
    def determine_round_winner(move_player_one: str, move_player_two: str, game: Game) -> str:
        """
        Determines the winner of a round based on the moves of two players.
        """
        if move_player_one == move_player_two:
            return "draw"

        if rules[move_player_one] == move_player_two:
            game.round_winned_player1 += 1
            return "player1"

        game.round_winned_player2 += 1
        return "player2"

    @staticmethod
    def determine_game_winner(game: Game) -> Optional[str] | None:
        """
        Determines the winner of the game based on the number of rounds won by each player.
        Returns the ID of the winning player if there is a winner, otherwise returns None.
        """
        if game.round_winned_player1 >= 3:
            return game.player1_id

        if game.round_winned_player2 >= 3:
            return game.player2_id

        return None
