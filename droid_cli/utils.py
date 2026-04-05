import sys


def print_header(title):
    """
    Prints a formatted header for CLI output.

    Args:
        title (str): The title to print as header.
    """
    print(f"{'=' * 10} {title} {'=' * 10}")


def print_error(message):
    """
    Prints an error message to the CLI in red.

    Args:
        message (str): The error message to print.
    """
    print(f"\033[91m{message}\033[0m")


def print_success(message):
    """
    Prints a success message to the CLI in green.

    Args:
        message (str): The success message to print.
    """
    print(f"\033[92m{message}\033[0m")


def print_warning(message):
    """
    Prints a warning message to the CLI in yellow.

    Args:
        message (str): The warning message to print.
    """
    print(f"\033[93m{message}\033[0m")


def print_info(message):
    """
    Prints an informational message to the CLI.

    Args:
        message (str): The informational message to print.
    """
    print(message)
