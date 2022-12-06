"""This file contains all the functions to be used in the sample-host app"""


def clean_string(input: str) -> str:
    """Convert the input to a string and strip any whitespace

    Example:
        >>> clean_string("  hello world  ")
        'hello world'

    Args:
        input (str): The input to clean

    Returns:
        str: The cleaned string
    """
    return str(input).strip()


def clean_int(input: str) -> int:
    """Convert the input to an integer

    Example:
        >>> clean_int("123")
        123

    Args:
        input (str): The input to clean

    Returns:
        int: The cleaned integer
    """
    return int(input)