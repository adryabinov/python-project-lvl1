#!/usr/bin/env python

import prompt


def welcome_user():

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(str.format('Hello, {}!', name))
    return name
