from brain_games.run.game_runner import run_game
from brain_games.run.functions import generate_above_100


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(int_number):
    PRIME_BEFORE_100 = {1, 2, 3, 5, 7, 11, 13, 17, 73, 79, 83, 89, 97}
    return int_number in PRIME_BEFORE_100


def generate_round():

    question = generate_above_100()

    if is_prime(question):
        answer = 'yes'
    else:
        answer = 'no'

    return str(question), answer


def run():
    run_game(generate_round, GAME_RULE)
