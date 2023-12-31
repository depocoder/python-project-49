#!/usr/bin/env python3
"""GCD script."""
from brain_games.cli import welcome_user
from brain_games.game_logic import game_loop
from brain_games.games.gcd import make_gcd_question


def main():
    """Cli GCD game."""
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    game_loop(make_gcd_question, name)


if __name__ == '__main__':
    main()
