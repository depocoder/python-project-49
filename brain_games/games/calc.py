"""Main logic of calc game."""
import random
from typing import Tuple

MAX_FIRST_DIGIT = 10
MAX_SECOND_DIGIT = 10


def make_calculate_question() -> Tuple[str, str]:
    """Create calculate question.

    Raises:
        ValueError: if operand is unsupported.
    """
    first_digit = random.randint(1, MAX_FIRST_DIGIT)
    second_digit = random.randint(1, MAX_SECOND_DIGIT)
    operation = random.choice(['+', '-', '*'])
    if operation == '+':
        answer = first_digit + second_digit
    elif operation == '-':
        answer = first_digit - second_digit
    elif operation == '*':
        answer = first_digit * second_digit
    else:
        raise ValueError("Can't find operator")
    question = f"{first_digit} {operation} {second_digit}"
    return question, str(answer)
