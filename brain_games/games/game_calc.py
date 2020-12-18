import random
from brain_games.engine import run


DESCRIPTION = 'What is the result of the expression?'
OPERATORS = ['+', '-', '*']


def calculate(first_int, second_int, operator):
    if operator == '+':
        return first_int + second_int
    elif operator == '-':
        return first_int - second_int
    else:
        return first_int * second_int


def generate_round():
    first_number = random.randint(1, 100)
    second_number = random.randint(1, 100)
    operator = random.choice(OPERATORS)
    question = (F'{first_number} {operator} {second_number}')
    answer = str(calculate(first_number, second_number, operator))
    return question, answer


def run_game():
    run(generate_round, DESCRIPTION)
