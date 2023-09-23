"""Main logic of calc game."""
import random
from typing import Tuple

MAX_START_PROGRESSION = 10
MAX_STEP_PROGRESSION = 10
MAX_LENGHT = 10


def make_progression_question() -> Tuple[str, str]:
    """Create arithmetic progression question."""
    start_progression = random.randint(1, MAX_START_PROGRESSION)
    step_progression = random.randint(1, MAX_STEP_PROGRESSION)
    lenght = random.randint(5, MAX_LENGHT)
    answer_index = random.randint(0, lenght - 1)
    progression = []
    for index in range(lenght):
        if index == answer_index:
            progression.append("..")
            continue
        progression.append(str((index * step_progression) + start_progression))
    question = " ".join(progression)
    answer = (answer_index * step_progression) + start_progression
    return question, str(answer)
