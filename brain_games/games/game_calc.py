import random
from brain_games.run.game_runner import run_game


GAME_RULE = 'What is the result of the expression?'


def calculate(first_int, second_int, operator):
    if operator == '+':
        return first_int + second_int
    elif operator == '-':
        return first_int - second_int
    else:
        return first_int * second_int


def generate_round():

    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])

    question = (F'{first_number} {operator} {second_number}')
    answer = calculate(first_number, second_number, operator)
    return question, str(answer)


def run():
    run_game(generate_round, GAME_RULE)
