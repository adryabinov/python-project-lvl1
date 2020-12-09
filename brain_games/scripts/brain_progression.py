#!/usr/bin/env python


import prompt
import random
from brain_games.games.game_progression import make_game
from brain_games.run.welcome_user import welcome_user
from brain_games.run.game_runner import runner
from brain_games.run.game_runner import game_iteration


def main():
    runner(make_game)


if __name__ == '__main__':
    main()