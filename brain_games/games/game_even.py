#!/usr/bin/env python

def make_game(seed):
    question_number = seed
    

    if question_number % 2 == 0:
        question_answer = 'yes'
    else:
        question_answer = 'no'
    return str(question_number), question_answer
