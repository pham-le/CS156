#!/usr/bin/python

"""
CS 156 Intro to AI - 01
Homework 2, 10/01/2014

Andres Chorro - 007340983
Jannette Pham-Le - 007855120
Justin Tieu - 007789678
"""

import random

print "Would you like to go first (1) or second (2)?"
turn = int(raw_input())
if turn == 1:
    print "You are first"
else:
    print "You are second"

deck = range(52)#build the deck (cards in order)
random.shuffle(deck)#shuffle the deck

player_hand = deck[-8:]#draw the last 8 cards
deck = deck[:-8]#take them out of the deck

computer_hand = deck[-8:]#computer draws the next 8
deck = deck[:-8]#take them out of the deck

print "player hand:", player_hand
print "computer hand:", computer_hand
print deck
