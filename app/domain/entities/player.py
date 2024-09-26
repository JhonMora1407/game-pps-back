"""Module app.domain.entities.player"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Player:
    """
    Player class representing a player entity.

    Attributes:
        - id (int): The unique identifier of the player.
        - fullname (str): The full name of the player.
        - created_at (datetime): The date and time when the player was created.
    """

    id: int = field(init=True)
    fullname: str = field(init=True)
    created_at: datetime = field(init=True, default=datetime.now)
