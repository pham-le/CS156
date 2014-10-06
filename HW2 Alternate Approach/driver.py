#!/usr/bin/python
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
    deck, human_hand, partial_state = state
    face_up_card, suit, computer_hand, history = partial_state
    print "\nCards in deck:", len(deck)
    print "Cards in opponent hand", len(computer_hand)
    print "History:", history
    print "Face up:", face_up_card
    print "Your hand:", human_hand
    print "Your options:", game.actions(partial_state)

print "Would you like to go first (1) or second (2)?"
current_player = int(raw_input()) - 1 #0 represents human, 1 for computer
human_turn = (current_player is 0) #true when it's the human's turn

current_state = game.get_initial_state(current_player)

if human_turn:
    print "You are first"
else:
    print "You are second"

while not game.game_over(current_state):
    while human_turn:
        printState(current_state)
        actions = game.actions(current_state[2], current_state[1])
        move = stringToMove(raw_input())
        if move not in actions:
            print "Invalid Move"
        else:
            current_state = game.result(current_state, move)
            human_turn = not human_turn
    
    print "\nCOMPUTER TURN:"
    print "COMPUTER OPTIONS:", current_state[2][]
    move = game.move_perfect_knowledge(current_state)
    print "COMPUTER MOVE:", move
    current_state = game.result(current_state, move)
    human_turn = not human_turn
#create variables that will be used to create the initial stat



