#!/usr/bin/env python

import random

GAME_RULE = 'What is the result of the expression?'


def make_game(seed=random.random()):

    first_number = int(seed * 10)
    second_number = int((seed * 100) % 10)
    operator_seed = int((seed * 1000) % 10)

    if operator_seed == (0 | 1 | 2 | 3):
        operator = '+'
        answer = first_number + second_number
    elif operator_seed == (4 | 5 | 6 | 7):
        operator = '-'
        answer = first_number - second_number
    else:
        operator = '*'
        answer = first_number * second_number

    question = str.format('{} {} {}', first_number, operator, second_number)

    return str(question), str(answer)
