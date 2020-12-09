#!/usr/bin/env python
import random

GAME_RULE = "rule_progression:TODO REWRITE"

def make_game(seed=random.random()):
    """seed = random return: TODO: qestion output format, game rule"""
    first_item = int(seed * 10)
    step = int((seed * 100) % 10)
    qestion_item_position = int((seed * 1000) % 10)
    progression = []

    for i in range(10):
        progression.append(first_item + (step * i))
        
    answer = progression[qestion_item_position]
    progression[qestion_item_position] = "..."
    question = str(progression)
    
    return str(question), str(answer)
