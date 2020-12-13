#!/usr/bin/env python
import random

GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def make_game(seed=random.random()):

    question = int(seed*1000)

    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return str(question), str(answer)
