#!/usr/bin/env python
import random

PRIME_BEFORE_100 = {1, 2, 3, 5, 7, 11, 13, 17, 73, 79, 83, 89, 97}
GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'

def make_game(seed=random.random()):
    """seed = random return: TODO: game rule, qestion string, answer,"""
    
    question = int(seed * 10)

    if question in PRIME_BEFORE_100:
        answer = 'yes'
    else:
        answer = 'no'
    
    return str(question), str(answer)