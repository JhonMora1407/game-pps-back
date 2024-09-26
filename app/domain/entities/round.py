"""Module app.domain.entities.round"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Round:
    """
    Round class represents a round in a game.

    Attributes:
        - id (int): The unique identifier of the round.
        - game_id (int): The identifier of the game the round belongs to.
        - player1_move (str): The move made by player 1 in the round.
        - player2_move (str): The move made by player 2 in the round.
        - round_game (int): The number of the round in the game.
        - winner (str): The winner of the round.
        - created_at (datetime): The timestamp when the round was created.
        - updated_at (datetime): The timestamp when the round was last updated.
    """

    id: int = field(init=True)
    game_id: int = field(init=True)
    player1_move: str = field(init=True)
    player2_move: str = field(init=True)
    round_game: int = field(init=True)
    winner: str = field(init=True)
    created_at: datetime = field(init=True, default=datetime.now)
    updated_at: datetime = field(init=True, default=datetime.now)
