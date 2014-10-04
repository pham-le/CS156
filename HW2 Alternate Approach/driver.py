#!/usr/bin/python
import random
from crazy_eights import CrazyEights

def stringToMove(string):
    """Converts a string that represents a move (eg: '(0, 25, 3, 0)')
    to an actual python tupple"""
    string = string.strip("()").replace(", ", " ").replace(",", " ").split()
    string = [int(s) for s in string]
    return tuple(string)

print "Would you like to go first (1) or second (2)?"
current_player = int(raw_input()) - 1 #0 represents human, 1 for computer
human_turn = (current_player == 0) #true when it's the human's turn
game = CrazyEights()
current_state = game.get_initial_state(current_player)

if human_turn:
    print "You are first"
else:
    print "You are second"

print current_state
#create variables that will be used to create the initial stat



