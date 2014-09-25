#!/usr/bin/python

"""
CS 156 Intro to AI - 01
Homework 2, 10/01/2014

Andres Chorro - 007340983
Jannette Pham-Le - 007855120
Justin Tieu - 007789678
"""

class CrazyEights:
    """A class that contains AI for crazy eights play"""
    def move(partial_state):
    def movePefectKnowedge(state):


hand = [] #without repeats in the range between 0 - 51
deck = [] #without repeats in the range between 0 - 51 representing the cards that are face down that have not been picked up by either player

state = () #tuple.. (deck, hand, partial_state), hand represents the other player's hand
partial_state = () #tuple.. (face_up_card, suit, hand, history), face_up_card = current card next move must be made on, history = [moves]
move = () #(player_num, face_up_card, suit, number_of_cards), faceupcard = card after the move, suit = next suit that must be played, numofcards = num of cards player picked up if any