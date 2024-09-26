"""Module app.domain.entities.game"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Game:
    """
    Game class represents a game between two players.

    Attributes:
        - id (int): The unique identifier of the game.
        - player1_id (int): The ID of the first player.
        - player2_id (int): The ID of the second player.
        - winner_id (int): The ID of the winner player.
        - round_winned_player1 (int): The number of rounds won by player 1.
        - round_winned_player2 (int): The number of rounds won by player 2.
        - created_at (datetime): The datetime when the game was created.
        - updated_at (datetime): The datetime when the game was last updated.
    """

    id: int = field(init=True)
    player1_id: int = field(init=True)
    player2_id: int = field(init=True)
    winner_id: int = field(init=True)
    current_round: int = field(init=True)
    round_winned_player1: int = field(init=True)
    round_winned_player2: int = field(init=True)
    created_at: datetime = field(init=True, default=datetime.now)
    updated_at: datetime = field(init=True, default=datetime.now)
