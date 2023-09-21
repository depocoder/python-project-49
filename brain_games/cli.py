"""Cli module."""
import prompt


def get_user():
    """Func for greetings user."""
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name
