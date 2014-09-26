#!/usr/bin/python

"""
CS 156 Intro to AI - 01
Homework 2, 10/01/2014

Andres Chorro - 007340983
Jannette Pham-Le - 007855120
Justin Tieu - 007789678
"""

import random

class CrazyEights:
	def __init__(self):
		"""A class that contains AI for crazy eights play"""
		self.deck = self.initializeDeck()				#builds and shuffles deck
		self.player_one_hand = self.initializeHand()	#draws 8 cards for player 1
		self.player_two_hand = self.initializeHand()	#draws 8 cards for player 2
		self.history = [] 								#new game contains no quadruple in its History

	def initializeDeck(self):
		""" without repeats in the range between 0 - 51 representing the cards that are face down that have not been picked up by either player """
		deck = range(52)								#build the deck (cards in order)
		random.shuffle(deck)							#shuffle the deck
		return deck

	def initializeHand(self):
		""" Helper function for constructor to grab initial hands from a deck without repeats in the range between 0 - 51"""
		hand = self.deck[-8:]							#draw the last 8 cards
		self.deck = self.deck[:-8]						#take them out of the deck
		return hand

	def appendHistory(self, move):
		""" 
			History appends a move that is a quadruple (player_num, face_up_card, suit, number_of_cards) 
			faceupcard = card after the move, suit = next suit that must be played, numofcards = num of cards player picked up if any
		"""
		self.history.append(move)

	def validMove(card, move):
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

	def move(self, partial_state):
		""" 
			Receives a partial_state that is a tuple (face_up_card, suit, hand, history)
			face_up_card = current card next move must be made on, history = [moves]
			Plays a card that is of the same suit or same number or an 8 
		"""		
		hand = partial_state[2]
		for card in hand:
			if validMove(card):
				return(1, card, card/13, 0)
		return(1, self.history[-1][1], self.history[-1][2],1)

	def movePefectKnowedge(self, state):
		""" Receives a tuple (deck, hand, partial_state), hand represents the other player's hand """
		return 

	def isGameOver(self):
		""" Checks if the game is over yet """
		return not(len(self.deck) > 0)