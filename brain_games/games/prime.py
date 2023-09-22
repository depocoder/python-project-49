"""Prime main game logic."""
import random

MAX_PRIME_DIGIT = 100


def make_prime_question():
    """Create prime digit question."""
    random_digit = random.randint(0, MAX_PRIME_DIGIT)
    if random_digit < 2:
        is_prime = False
    else:
        is_prime = True
    for digit in range(2, random_digit):
        if random_digit % digit == 0:
            is_prime = False
            break
    answer = 'yes' if is_prime else 'no'
    return random_digit, answer
