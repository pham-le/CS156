#!/usr/bin/python

"""
CS 156 Intro to AI - 01
Homework 2, 10/01/2014

Andres Chorro - 007340983
Jannette Pham-Le - 007855120
Justin Tieu - 007789678
"""

from crazy_eights import CrazyEights


def stringToMove(string):
    """Converts a string that represents a move (eg: '(0, 25, 3, 0)')
    to an actual python tupple"""
    string = string.strip("()").replace(", ", " ").replace(",", " ").split()
    string = [int(s) for s in string]
    return tuple(string)


print "Would you like to go first (1) or second (2)?"
turn = int(raw_input()) - 1  # player is 0, computer is 1
if turn == 0:
    print "You are first"
else:
    print "You are second"

# alias
ce = CrazyEights(turn)  #creates a Crazy Eights game
deck = ce.deck
player_hand = ce.player_one_hand
computer_hand = ce.player_two_hand

print "Your hand:", player_hand

while True:
    print ce.history
    print "Enter your move (0, card you're playing, suit you're changing to, 0)"
    move = stringToMove(raw_input())  #input the human's move
    if ce.validMove(move[1]):
        ce.executeMove(move)
        print ce.history
        print "Your updated hand:", player_hand
        break
    else:
        print "Your move is invalid"
