#!/usr/bin/env python3
"""Progression script."""
from brain_games.cli import get_user
from brain_games.game_logic import game_loop
from brain_games.games.progression import make_progression_question


def main():
    """Cli progression game."""
    print("Welcome to the Brain Games")
    name = get_user()
    print('What number is missing in the progression?')
    game_loop(make_progression_question, name)


if __name__ == '__main__':
    main()
