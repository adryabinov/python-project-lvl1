import random
from brain_games.engine import run


DESCRIPTION = 'What is the result of the expression?'
OPERATORS_FUNC = {'+': lambda x,y: x + y,
            '-': lambda x,y: x - y, 
            '*': lambda x,y: x * y}
OPERATORS_LIST = list(OPERATORS_FUNC.keys())


def generate_round():
    first_number = random.randint(1, 10)
    second_number = random.randint(1, 10)
    operator = random.choice(OPERATORS_LIST)
    question = (F'{first_number} {operator} {second_number}')
    answer = str(OPERATORS_FUNC[operator](first_number, second_number))
    return question, answer


def run_game():
    run(generate_round, DESCRIPTION)
