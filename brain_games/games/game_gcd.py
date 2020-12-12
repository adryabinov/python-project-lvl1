#!/usr/bin/env python
import random

PRIME_11 = [1, 2, 3, 5, 7, 11, 13, 17, 73, 79]
GAME_RULE = 'Find the greatest common divisor of given numbers.'

def make_game(seed=random.random()):
    first_pos = int(seed * 10)
    second_pos = int((seed * 100) % 10)

    if first_pos == second_pos & first_pos: #for diff numbers
        second_pos += 1

    num = int((seed * 1000) % 10) + 1 #1-10
    question = str.format('{} {}', num * PRIME_11[first_pos], num * PRIME_11[second_pos])
    answer = num
    return str(question), str(answer)