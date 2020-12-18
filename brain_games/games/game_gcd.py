import random
from math import gcd
from brain_games.engine import run


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    first_num = random.randint(1, 100)
    second_num = random.randint(1, 100)
    question = (F'{first_num} {second_num}')
    answer = str(gcd(first_num, second_num))

    return question, answer


def run_game():
    run(generate_round, DESCRIPTION)
