"""Cli module."""
import logging

import prompt

logger = logging.getLogger(__name__)


def welcome_user():
    """Func for greetings user."""
    name = prompt.string('May I have your name? ')
    logger.info(f"Hello, {name}!")
    return name
