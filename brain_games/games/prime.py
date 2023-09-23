"""Prime main game logic."""
import random
from typing import Tuple

MAX_PRIME_NUMBER = 100


def is_prime_number(number) -> bool:
    """Check if number is prime.

    Args:
        number: number which we need to check
    """
    is_prime = True
    if number < 2:
        is_prime = False
    for loop_number in range(2, number):
        if number % loop_number == 0:
            is_prime = False
            break
    return is_prime


def make_prime_question() -> Tuple[str, str]:
    """Create prime number question."""
    random_number = random.randint(0, MAX_PRIME_NUMBER)
    answer = 'yes' if is_prime_number(random_number) else 'no'
    return str(random_number), answer
