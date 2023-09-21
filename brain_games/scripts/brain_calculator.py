#!/usr/bin/env python3
"""Calculator script."""
from brain_games.cli import welcome_user
from brain_games.game_logic import game_loop
from brain_games.games.calc import make_calculate_question


def main():
    """Cli caclulator game."""
    print("Welcome to the Brain Games")
    name = welcome_user()
    print("What is the result of the expression?")
    game_loop(make_calculate_question, name)


if __name__ == '__main__':
    main()
