import prompt

ROUNDS_TO_WIN = 3


def run_round__is_win(round, user_name):

    (question, answer) = round()
    WIN_ROUND_MSG = 'Correct!'
    LOSE_ROUND_MSG = (F'is wrong answer ;(. \
Correct answer was "{answer}".\n\
Let\'s try again, {user_name}!')

    print(F'Question: {question}')
    user_answer = prompt.string('Your answer: ')
    if user_answer == answer:
        print(WIN_ROUND_MSG)
        return True
    else:
        print(F'"{user_answer}" {LOSE_ROUND_MSG}')
        return False


def run_game(game_round, game_rules):

    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(F'Hello, {user_name}!')

    print(game_rules)
    for _ in range(ROUNDS_TO_WIN):
        if not run_round__is_win(game_round, user_name):
            return
    print(F'Congratulations, {user_name}!')
