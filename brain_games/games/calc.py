"""Main logic of calc game."""
import random

MAX_FIRST_DIGIT = 10
MAX_SECOND_DIGIT = 10


def make_calculate_question():
    """Create calculate question."""
    first_digit = random.randint(1, MAX_FIRST_DIGIT)
    second_digit = random.randint(1, MAX_SECOND_DIGIT)
    operation = random.choice(['+', '-', '*'])
    if operation == '+':
        answer = first_digit + second_digit
    elif operation == '-':
        answer = first_digit - second_digit
    else:
        answer = first_digit * second_digit
    question = f"{first_digit} {operation} {second_digit}"
    return question, answer
