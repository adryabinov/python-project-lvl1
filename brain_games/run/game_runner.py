#!/usr/bin/env python

import random
import prompt
from brain_games.run.welcome_user import welcome_user

def game_iteration(game, user_name):
    (question, answer) = game
    game_rules_string = 'Answer "yes" if the number is even, otherwise answer "no".'
    win_message = 'Correct!'
    loose_message = "is wrong answer ;(. Correct answer was \"" + answer + "\".\nLet's try again, " + user_name + "!"

    print(game_rules_string)
    print('Question:', question)
    user_answer = prompt.string('Your answer: ')
    if user_answer == answer:
        print(win_message)
        return True
    else:
        print("\"" + user_answer + "\"", loose_message)
        return False

def runner(game_maker):
    user_name = welcome_user()
    ROUNDS_TO_WIN = 3
    rounds_left = 0

    while rounds_left < ROUNDS_TO_WIN:
        game = game_iteration(game_maker(random.random()), user_name)
        if game:
            rounds_left = rounds_left + 1
        else:
            return False
    return True