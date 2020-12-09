#!/usr/bin/env python

#TODO: reformat strings (remove concat), check style

import random
import prompt
from brain_games.run.welcome_user import welcome_user

def game_iteration(game, user_name):
    (question, answer) = game
    win_message = 'Correct!'
    lose_message = "is wrong answer ;(. Correct answer was \"" + answer + "\".\nLet's try again, " + user_name + "!"

    print('Question:', question)
    user_answer = prompt.string('Your answer: ')
    if user_answer == answer:
        print(win_message)
        return True
    else:
        print("\"" + user_answer + "\"", lose_message)
        return False

def runner(game_maker, rules):
    user_name = welcome_user()
    ROUNDS_TO_WIN = 3
    rounds_left = 0
    print(rules)
    while rounds_left < ROUNDS_TO_WIN:
        game = game_iteration(game_maker(random.random()), user_name)
        if game:
            rounds_left = rounds_left + 1
        else:
            return False
    print("Congratulations, " + user_name + "!" )
    return True