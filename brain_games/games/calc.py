import random
from brain_games.engine import run


DESCRIPTION = 'What is the result of the expression?'
MAP_OPERATORS_TO_OPERATIONS = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
}


def generate_round():
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    operator = random.choice(list(MAP_OPERATORS_TO_OPERATIONS.keys()))
    question = F'{first_number} {operator} {second_number}'
    answer = MAP_OPERATORS_TO_OPERATIONS[operator](
        first_number,
        second_number)
    return question, str(answer)


def run_game():
    run(generate_round, DESCRIPTION)
