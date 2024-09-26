"""Module app.utils.decorators"""

from functools import wraps

from app.utils.exceptions import handle_exception


def handle_exceptions(func):
    """
    Decorator function that handles exceptions raised by the decorated function.

    Parameters:
        - func: The function to be decorated.

    Returns:
        - The decorated function.
    """

    @wraps(func)
    def decorated_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return handle_exception(e)

    return decorated_function
