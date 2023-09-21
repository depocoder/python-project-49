"""Main logic of even game."""
import random
from typing import Tuple

MAX_EVEN_DIGIT = 100


def make_even_question() -> Tuple[int, str]:
    """Make even question."""
    random_digit = random.randint(1, MAX_EVEN_DIGIT)
    is_even = random_digit % 2 == 0
    answer = 'yes' if is_even else 'no'
    return random_digit, answer
