#!/usr/bin/env python

import prompt

def welcome_user():
    """GET user name and say HI, RETURN INPUT STR (NAME)"""

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')
    return name