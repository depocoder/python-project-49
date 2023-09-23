"""Main logic of GCD game."""
import random
from typing import Tuple

MAX_GCD_FIRST_DIGIT = 10
MAX_GCD_SECOND_DIGIT = 10


def find_gcd(min_digit: int, max_digit: int):
    """Find the greatest common divisor.

    Args:
        min_digit: Smaller digit than max_digit
        max_digit: Bigger digit than min_digit
    """
    for digit in range(min_digit, 0, -1):
        if min_digit % digit == 0 and max_digit % digit == 0:
            return digit


def make_gcd_question() -> Tuple[str, str]:
    """Create the greatest common divisor question."""
    first_digit = random.randint(1, MAX_GCD_FIRST_DIGIT)
    second_digit = random.randint(1, MAX_GCD_SECOND_DIGIT)
    if first_digit > second_digit:
        gcd_digit = find_gcd(first_digit, second_digit)
    elif second_digit > first_digit:
        gcd_digit = find_gcd(second_digit, first_digit)
    else:
        gcd_digit = first_digit
    return f"{first_digit} {second_digit}", str(gcd_digit)
