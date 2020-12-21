import random
from brain_games.engine import run


DESCRIPTION = 'What is the result of the expression?'
map_operators_to_operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
}


def generate_round():
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    operator = random.choice(list(map_operators_to_operations.keys()))
    question = F'{first_number} {operator} {second_number}'
    answer = map_operators_to_operations[operator](
        first_number,
        second_number)
    return question, str(answer)


def run_game():
    run(generate_round, DESCRIPTION)
