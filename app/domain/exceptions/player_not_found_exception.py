"""Module app.domain.exceptions.player_not_found_exception"""


class PlayerNotFoundException(Exception):
    """
    Represents an exception raised when a player is not found.

    Attributes:
        - message (str): The message of the exception.
    """

    def __init__(self, player_id: int) -> None:
        """
        Initializes the exception.

        Parameters:
            - message (str): The message of the exception.
        """
        message = f"Player with id {player_id} not found"
        super().__init__(message)
