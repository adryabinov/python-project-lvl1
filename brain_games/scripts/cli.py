#!/usr/bin/env python


import prompt


def welcome_user():
    """GET user name and say HI"""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')


def main():
    welcome_user()


if __name__ == '__main__':
    main()
