#!/usr/bin/env python

from brain_games.games.game_gcd import make_game
from brain_games.games.game_gcd import GAME_RULE

from brain_games.run.game_runner import runner


def main():
    runner(make_game, GAME_RULE)


if __name__ == '__main__':
    main()
