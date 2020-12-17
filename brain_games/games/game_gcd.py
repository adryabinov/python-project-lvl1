from math import gcd
from brain_games.run.game_runner import run_game
from brain_games.run.functions import generate_above_100


GAME_RULES = 'Find the greatest common divisor of given numbers.'


def generate_round():

    first_num = generate_above_100()
    second_num = generate_above_100()

    question = (F'{first_num} {second_num}')
    answer = str(gcd(first_num, second_num))

    return question, answer


def run():
    run_game(generate_round, GAME_RULES)
