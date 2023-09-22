#!/usr/bin/env python3
"""Prime script."""
from brain_games.cli import welcome_user
from brain_games.game_logic import game_loop
from brain_games.games.prime import make_prime_question


def main():
    """Cli prime game."""
    name = welcome_user()
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")
    game_loop(make_prime_question, name)


if __name__ == '__main__':
    main()
