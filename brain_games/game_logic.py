"""Additional game logic."""


def is_answer_correct(random_digit, user_answer):
    is_even = (random_digit % 2) == 0
    correct_answer = "yes" if is_even else "no"
    if correct_answer == user_answer:
        return True
    print(
        f"'{user_answer}' is wrong answer ;(. "
        f"Correct answer was '{correct_answer}'.",
    )
    return False
