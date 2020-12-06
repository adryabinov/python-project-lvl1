#!/usr/bin/env python

import prompt

def welcome_user():
    """PUT TO CONSOLE GREAT MSG, RETURN USER INPUT STR (NAME)"""

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name