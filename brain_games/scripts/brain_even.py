#!/usr/bin/env python3
"""Main braing games module."""
import random

import prompt

from brain_games.cli import welcome_user
from brain_games.game_logic import is_answer_correct


def main():
    name = welcome_user()
    consecutive_wins = 0
    wins_for_end = 3
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    while consecutive_wins != wins_for_end:
        random_digit = random.randint(1, 100)
        print(f"Question: {random_digit}")
        user_answer = prompt.string('Your answer: ').lower()
        if is_answer_correct(random_digit, user_answer):
            print("Correct")
            consecutive_wins += 1
            continue

        print(f"Let's try again, {name}!")
        consecutive_wins = 0

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    main()
