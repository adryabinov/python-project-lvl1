import random
from brain_games.engine import run


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number == 1:
        return False
    for i in range(2, number):
        if (number % i == 0):
            return False
    return True


def generate_round():
    question = random.randint(1, 100)
    answer = 'yes' if is_prime(question) else 'no'
    return str(question), answer


def run_game():
    run(generate_round, DESCRIPTION)
