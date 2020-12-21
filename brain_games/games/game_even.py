import random
from brain_games.engine import run

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    question = random.randint(1, 100)
    answer = 'yes' if is_even(question) else 'no'
    return str(question), answer


def run_game():
    run(generate_round, DESCRIPTION)
