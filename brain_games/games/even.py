"""Main logic of even game."""
import random
from typing import Tuple

MAX_EVEN_NUMBER = 100


def make_even_question() -> Tuple[str, str]:
    """Make even question."""
    random_number = random.randint(1, MAX_EVEN_NUMBER)
    is_even = random_number % 2 == 0
    answer = 'yes' if is_even else 'no'
    return str(random_number), answer
