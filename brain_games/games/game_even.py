#!/usr/bin/env python


import random
from brain_games.run.game_runner import run_game
from brain_games.run.game_runner import run_round__is_win

GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(int_number):
    return int_number % 2 == 0


def generate_round():

    question = random.randint(1,100)

    if is_even(question):
        answer = 'yes'
    else:
        answer = 'no'
    return str(question), answer

def run():
    run_game(generate_round,GAME_RULES)
