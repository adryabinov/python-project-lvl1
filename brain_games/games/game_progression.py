#!/usr/bin/env python
import random


def make_game(seed=random.random()):
    """seed = random return: TODO: qestion output format, game rule"""
    game_rules = "rule_progression:TODO REWRITE"
    first_item = int(seed * 10)
    step = int((seed * 100) % 10)
    qestion_item_position = int((seed * 1000) % 100 // 10)
    progression = []

    for i in range(10):
        progression.append(first_item + (step * i))
    question_answer = progression[qestion_item_position]
    progression[qestion_item_position] = "..."
    question = str(progression)
    
    return question, str(question_answer), game_rules
