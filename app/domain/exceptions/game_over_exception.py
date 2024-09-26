"""Module app.domain.exceptions.game_exception"""


class GameOverException(Exception):
    """
    Represents an exception raised when an error occurs in a game.

    Attributes:
        - message (str): The message of the exception.
    """

    def __init__(self, player: str) -> None:
        """
        Initializes the exception.

        Parameters:
            - message (str): The message of the exception.
        """
        message = f"The {player} is the new champion!!!"
        super().__init__(message)
