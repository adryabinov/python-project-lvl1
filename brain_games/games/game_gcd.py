import random
from math import gcd
from brain_games.engine import run


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_round():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    question = (F'{first_number} {second_number}')
    answer = str(gcd(first_number, second_number))

    return question, answer


def run_game():
    run(generate_round, DESCRIPTION)
