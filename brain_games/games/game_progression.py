#!/usr/bin/env python
import random
from brain_games.run.game_runner import run_game

GAME_RULES = 'What number is missing in the progression?'

def make_progression_arr(start, step):
    progression = []

    for i in range(10):
        progression.append(start + (step * i))
    return progression

def generate_round():

    first_item = random.randint(1, 10)
    step = random.randint(1, 10)
    question_item_position = random.randint(0, 9)
    progression = make_progression_arr(first_item, step)

    answer = str(progression[question_item_position])
    progression[question_item_position] = '...'
    question = ' '.join([str(elem) for elem in progression])

    return question, answer


def run():
    run_game(generate_round,GAME_RULES)