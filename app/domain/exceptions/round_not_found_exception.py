"""Module app.domain.exceptions.round_not_found_exception"""


class RoundNotFoundException(Exception):
    """
    Represents an exception raised when a game is not found.

    Attributes:
        - message (str): The message of the exception.
    """

    def __init__(self, game_id: int) -> None:
        """
        Initializes the exception.

        Parameters:
            - message (str): The message of the exception.
        """
        message = f"Rounds with game id {game_id} not found"
        super().__init__(message)
