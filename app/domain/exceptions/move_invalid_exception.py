"""Module app.domain.exceptions.move_invalid_exception"""


class MoveInvalidException(Exception):
    """
    Represents an exception raised when a player makes an invalid move.

    Attributes:
        - message (str): The message of the exception.
    """

    def __init__(self, moves: str) -> None:
        """
        Initializes the exception.

        Parameters:
            - message (str): The message of the exception.
        """
        message = f"Invalid value. Valid moves are: {', '.join(moves)}"
        super().__init__(message)
