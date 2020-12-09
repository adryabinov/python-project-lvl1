#!/usr/bin/env python
import random

GAME_RULE = "even rule: TODO REWRITE"

def make_game(seed=random.random()):
    """seed = random return: TODO: game rule, qestion string, answer,"""
    
    question = int(seed*1000)
    

    if question % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return str(question), str(answer) 
