#! /usr/bin/env python3
# coding: utf-8
'''This is a game round in the while loop'''
from play_game import *

py.init()
level = 0
life_num = 5

while level <= 10 and life_num != 0:
    play = play_game(level, life_num)
    if play == 'win':
        level += 1
    elif play == 'quit':
        life_num = 0
    else:
        life_num -= 1
