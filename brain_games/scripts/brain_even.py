#!/usr/bin/env python3
"""Even script."""
from brain_games.cli import welcome_user
from brain_games.game_logic import game_loop, make_even_question


def main():
    name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    game_loop(make_even_question, name)


if __name__ == '__main__':
    main()
