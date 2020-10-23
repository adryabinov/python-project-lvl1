#!/usr/bin/env python


import random


def make_game():
    qestion_number = random.randrange(1000)
    if qestion_number % 2 == 0:
        qestion_answer = 'yes'
    else:
        qestion_answer = 'no'
    return (str(qestion_number) , qestion_answer)


def main():
    make_game()


if __name__ == '__main__':
    main()