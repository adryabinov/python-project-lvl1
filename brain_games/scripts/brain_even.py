#!/usr/bin/env python


import prompt, random


#dialog's strings
game_rules_string = 'Answer "yes" if the number is even, otherwise answer "no".'
win_message = 'Correct!'
loose_message = "is wrong answer ;(. Correct answer was 'no'.\nLet's try again, Bill!"


#game settings
rounds_to_win = 3

def welcome_user():
    """GET user name and say HI"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name

def make_game():
    qestion_number = random.randrange(1000)
    if qestion_number % 2 == 0:
        qestion_answer = 'yes'
    else:
        qestion_answer = 'no'
    return (str(qestion_number) , qestion_answer)

def game_iteration(game):
    (qestion, answer) = game
    print(game_rules_string)
    print('Qestion:',qestion)
    user_answer = prompt.string('Your answer: ')
    if user_answer == answer:
        print(win_message)
        return True
    else:
        print("'" + user_answer + "'", loose_message)
        return False



def main():
    rounds_to_win = 3
    #welcome_user()
    while rounds_to_win > 0:
        game = game_iteration(make_game())
        if  game == False:
            return False
        else:
            rounds_to_win = rounds_to_win - 1
    return True 
        


if __name__ == '__main__':
    main()