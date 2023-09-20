#!/usr/bin/env python3
"""Main braing games module."""
from brain_games.cli import welcome_user
from brain_games.game_logic import game_loop, make_calculate_question


def main():
    name = welcome_user()
    print("What is the result of the expression?")
    game_loop(make_calculate_question, name)


if __name__ == '__main__':
    main()
