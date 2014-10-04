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

# creates a Crazy Eights game
ce = CrazyEights(turn)

while not ce.isGameOver():
    print "\n\nGame History:", ce.history
    while True and ce.currentPlayer == 0:
        print "Cards left in deck:", len(ce.deck)
        print "Cards left in computer hand:", len(ce.computer_hand)
        print "Face up card:", ce.history[-1][1]
        print "Your current hand:", ce.human_hand
        print "Enter your move (0, card you're playing, suit you're changing to, 0):"


        # input the human's move
        move = stringToMove(raw_input())

        if ce.validMove(move):
            ce.executeMove(move)
            print "Your updated hand:", ce.human_hand
            break
        else:
            print "Your move is invalid"

    if ce.isGameOver(): #check for end after player's turn
        break

    if(ce.currentPlayer == 1):
        print "\nComputer's turn"
        # partial_state that is a tuple (face_up_card, suit, hand, history)
        face_up_card = ce.history[-1][1]
        suit = ce.history[-1][2]
        partial_state = (face_up_card, suit, ce.computer_hand, ce.history)
        computer_move = ce.move(partial_state)

        # checks if given move is the last move in history. if it is, end game
        if computer_move in ce.history:
            break
        else:
            ce.executeMove(computer_move)
        print("End of Computer's turn")
print ce.getWinner()
