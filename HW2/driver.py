#!/usr/bin/python

"""
CS 156 Intro to AI - 01
Homework 2, 10/01/2014

Andres Chorro - 007340983
Jannette Pham-Le - 007855120
Justin Tieu - 007789678
"""

import random

def ValidMove(card, move):
    """returns true if card (the card being played) is legally
    playable after move"""
    face_up = move[1]
    if((card - 7) % 13 == 0): #card is an 8, always playable
        return True

    elif(card / 13 == face_up / 13): #cards are the same suit
        return True

    elif(card % 13 == card % 13): #cards are the same value
        return True

    else:
        return False

def stringToMove(string):
    """Converts a string that represents a move (eg: '(0, 25, 3, 0)')
    to an actual python tupple"""
    string = string.strip("()").replace(",", "").split()
    string = [int(s) for s in string]
    return tuple(string)

print "Would you like to go first (1) or second (2)?"
turn = int(raw_input()) - 1 #player is 0, computer is 1
if turn == 0:
    print "You are first"
else:
    print "You are second"

deck = range(52)#build the deck (cards in order)
random.shuffle(deck)#shuffle the deck

player_hand = deck[-8:]#draw the last 8 cards
deck = deck[:-8]#take them out of the deck

computer_hand = deck[-8:]#computer draws the next 8
deck = deck[:-8]#take them out of the deck

last_move = (1, deck.pop(), 0, 0)#represents the initial "non-move" that starts the game
history = [last_move]

print "Last move:", last_move
print "Your hand:", player_hand

while True:
    print "Enter your move (0, card you're playing, suit you're changing to, 0)"
    move = stringToMove(raw_input())#input the human's move
    if ValidMove(move[1], last_move):
        history.append(last_move)
        print history
        break
    else:
        print "Your move is invalid"
