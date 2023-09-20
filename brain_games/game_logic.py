"""Additional game logic."""
import random

import prompt

WINS_TO_END = 3


def is_answer_correct(user_answer, correct_answer):
    if str(correct_answer) == user_answer:
        return True
    print(
        f"'{user_answer}' is wrong answer ;(. "
        f"Correct answer was '{correct_answer}'.",
    )
    return False


def make_calculate_question():
    first_random_digit = random.randint(1, 100)
    second_random_digit = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    if operation == '+':
        answer = first_random_digit + second_random_digit
    elif operation == '-':
        answer = first_random_digit - second_random_digit
    else:
        answer = first_random_digit * second_random_digit
    question = f"{first_random_digit} {operation} {second_random_digit}"
    return question, answer


def make_even_question():
    random_digit = random.randint(1, 100)
    is_even = random_digit % 2 == 0
    answer = 'yes' if is_even else 'no'
    return random_digit, answer


def game_loop(make_question, name):
    consecutive_wins = 0
    while consecutive_wins != WINS_TO_END:
        question, answer = make_question()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ').lower()
        if is_answer_correct(user_answer.lower(), answer):
            print("Correct")
            consecutive_wins += 1
            continue

        print(f"Let's try again, {name}!")
        consecutive_wins = 0

    print(f"Congratulations, {name}!")
