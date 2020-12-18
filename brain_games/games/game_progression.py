#!/usr/bin/env python
import random
from brain_games.engine import run


DESCRIPTION = 'What number is missing in the progression?'
TERM_MASK = '..'


def randomize_progression_init():
    initial_term = random.randint(1, 10)
    difference = random.randint(1, 10)
    return initial_term, difference


def make_progression_fix_length(initiators, length):
    progression = []
    initial_term, difference = initiators
    for i in range(length):
        progression.append(initial_term + (difference * i))
    return progression


def get_masked_elem_list(list, elem_position, mask):
    return list[:elem_position] + [mask] + list[elem_position + 1:]


def generate_round():
    progression_length = random.randint(5, 10)
    random_term_position = random.randint(0, progression_length - 1)
    progression = make_progression_fix_length(
        randomize_progression_init(), progression_length)
    answer = str(progression[random_term_position])
    question = ' '.join(
        [str(elem) for elem in get_masked_elem_list(progression,
                                                    random_term_position,
                                                    TERM_MASK)])
    return question, answer


def run_game():
    run(generate_round, DESCRIPTION)
