#!/usr/bin/env python


import prompt, random

game_rules_string = 'Answer "yes" if the number is even, otherwise answer "no".'
win_message = 'Correct!'
loose_message = "is wrong answer ;(. Correct answer was 'no'./nLet's try again, Bill!" 

def make_game():
    qestion_number = random.randrange(1000)
    if qestion_number % 2 == 0:
        qestion_answer = 'yes'
    else:
        qestion_answer = 'no'
    return (str(qestion_number) , qestion_answer)

def user_game_dialog(game):
    (qestion, answer) = game
    print(game_rules_string)
    print('Qestion:',qestion)
    user_answer = prompt.string('Your answer: ')
    if user_answer == answer:
        print(win_message)
    else:
        print("'" + answer + "'", loose_message)



def main():
    user_game_dialog(make_game())


if __name__ == '__main__':
    main()