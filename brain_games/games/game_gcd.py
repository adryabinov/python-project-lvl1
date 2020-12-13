#!/usr/bin/env python
import random
from math import gcd

GAME_RULE = 'Find the greatest common divisor of given numbers.'

def make_game(seed=random.random()):
    first_num = int(seed * 100)
    second_num = int((seed * 10000) % 100)
    question = str.format('{} {}', first_num, second_num)
    answer = gcd(first_num, second_num)

    return str(question), str(answer)