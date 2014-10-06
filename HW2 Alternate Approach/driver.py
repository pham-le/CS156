#!/usr/bin/python

"""
CS 156 Intro to AI - 01
Homework 2, 10/01/2014

Andres Chorro - 007340983
Jannette Pham-Le - 007855120
Justin Tieu - 007789678
"""

import random
from crazy_eights import CrazyEights

game = CrazyEights()


def stringToMove(string):
    """Converts a string that represents a move (eg: '(0, 25, 3, 0)')
    to an actual python tupple"""
    string = string.strip("()").replace(", ", " ").replace(",", " ").split()
    string = [int(s) for s in string]
    return tuple(string)


def printState(state):
    deck, opponent_hand, partial_state = state
    face_up_card, suit, your_hand, history = partial_state
    print "\nCards in deck:", len(deck)
    print "Opponent hand:", opponent_hand
    print "History:", history
    print "Face up:", face_up_card
    print "Your hand:", your_hand
    print "Your options:", game.actions(partial_state)


print "Would you like to go first (1) or second (2)?"
current_player = int(raw_input()) - 1  # 0 represents human, 1 for computer
human_turn = (current_player is 0)  # true when it's the human's turn

current_state = game.get_initial_state(current_player)

if human_turn:
    print "You are first"
else:
    print "You are second"

while not game.game_over(current_state):
    if human_turn:
        print "\nHUMAN TURN:"
        printState(current_state)
        actions = game.actions(current_state[2])
        move = stringToMove(raw_input())
        while move not in actions:
            print "Invalid Move"
            move = stringToMove(raw_input())
        current_state = game.result(current_state, move)
        human_turn = not human_turn
    else:
        print "\nCOMPUTER TURN:"
        printState(current_state)
        move = game.dumb_move(current_state)
        print "COMPUTER MOVE:", move
        current_state = game.result(current_state, move)
        human_turn = not human_turn

printState(current_state)
if game.utility(current_state, 0) is 1:
    print "\nHUMAN WINS!"
else:
    print "\nCOMPUTER WINS!"
# create variables that will be used to create the initial stat



