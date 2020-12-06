#!/usr/bin/env python


import prompt
import random
from brain_games.games.game_even import make_game
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


def main():
    user_name = welcome_user()
    rounds_to_win = 3

    while rounds_to_win > 0:
        game = game_iteration(make_game(random.randrange(1000)), user_name)
        if game:
            rounds_to_win = rounds_to_win - 1
        else:
            return False
    return True


if __name__ == '__main__':
    main()
