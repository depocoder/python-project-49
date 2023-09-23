"""Main game logic."""

import prompt

WINS_TO_END = 3


def game_loop(make_question, name):
    """Main game loop.

    Args:
        make_question: func for creating question.
        name: name of user
    """
    consecutive_wins = 0
    for _ in range(0, WINS_TO_END):
        question, answer = make_question()
        print(f"Question: {question}")
        user_answer = prompt.string('Your answer: ').lower()
        if user_answer == str(answer):
            print("Correct")
            consecutive_wins += 1
            continue
        print(
            f"'{user_answer}' is wrong answer ;(. "
            f"Correct answer was '{answer}'.",
        )
        print(f"Let's try again, {name}!")
        return

    print(f"Congratulations, {name}!")
