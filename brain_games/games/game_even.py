#!/usr/bin/env python
import random


def make_game(seed=random.random()):
    """seed = random return: TODO: game rule, qestion string, answer,"""

    question_number = int(seed*1000)
    

    if question_number % 2 == 0:
        question_answer = 'yes'
    else:
        question_answer = 'no'
    return str(question_number), question_answer
