#!/usr/bin/env python
import random


def make_game(seed=random.random()):
    """seed = random return: TODO: game rule, qestion string, answer,"""
    PRIME_BEFORE_100 = {1, 2, 3, 5, 7, 11, 13, 17, 73, 79, 83, 89, 97}
    game_rules = "prime rule: TODO REWRITE"
    question = int(seed * 10)

    if question in PRIME_BEFORE_100:
        answer = "yes"
    else:
        answer = "no"
    
    return str(question), str(answer), str(game_rules)