import random
from brain_games.engine import run


DESCRIPTION = 'What number is missing in the progression?'
TERM_MASK = '..'


def make_progression(
        length,
        initial_term,
        difference):
    progression = []
    for i in range(length):
        progression.append(initial_term + (difference * i))
    return progression


def make_question(progression, position, mask=TERM_MASK):
    masked_progression = progression[:]
    masked_progression[position] = mask
    return ' '.join([str(elem) for elem in masked_progression])


def generate_round():
    progression_length = random.randint(5, 10)
    answer_term_position = random.randint(0, progression_length - 1)
    progression = make_progression(
        length=progression_length,
        initial_term=random.randint(1, 10),
        difference=random.randint(1, 10)
        )
    answer = progression[answer_term_position]
    question = make_question(progression, answer_term_position)
    return question, str(answer)


def run_game():
    run(generate_round, DESCRIPTION)
