#!/usr/bin/env python

import random
import prompt

from brain_games.run.welcome_user import welcome_user


def game_iteration(game, user_name):

    (question, answer) = game

    win_message = 'Correct!'
    lose_message_form = 'is wrong answer ;(. \
                        Correct answer was "{}".\
                        \nLet\'s try again, {}!'

    lose_message = str.format(lose_message_form, answer, user_name)

    print(str.format('Question: {}', question))
    user_answer = prompt.string('Your answer: ')
    if user_answer == answer:
        print(win_message)
        return True
    else:
        print(str.format('"{}" {}', user_answer, lose_message))
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
    print(str.format('Congratulations, {}!', user_name))
    return True
