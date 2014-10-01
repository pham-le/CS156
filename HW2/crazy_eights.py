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
    def __init__(self, currentPlayer):
        """A class that contains AI for crazy eights play"""
        self.deck = self.initializeDeck()  # builds and shuffles deck
        self.currentPlayer = currentPlayer
        self.human_hand = []
        self.computer_hand = []
        self.draw(0, 8)# draws 8 cards for player 1
        self.draw(1, 8)  # draws 8 cards for player 2
        self.history = self.initializeHistory()  # new game contains no quadruple in its History

    def initializeDeck(self):
        """ without repeats in the range between 0 - 51 representing the cards that are face down that have not been picked up by either player """
        deck = range(52)  # build the deck (cards in order)
        random.shuffle(deck)  # shuffle the deck
        return deck

    def initializeHistory(self):
        """ Helper function for constructor to make the first "non-move" and start the face-up pile"""
        card = self.deck.pop()
        return [(self.currentPlayer, card, card / 13, 0)]

    def draw(self, playernum, numCards):
    	""" Helper function to draw numcards number of cards from the deck
        for player payernum (0 for human, 1 for computer)"""
        cards = self.deck[-1 * numCards:]
        self.deck = self.deck[:-1 * numCards]
        if playernum == 0:
            self.human_hand = self.human_hand + cards
        else:
            self.computer_hand = self.computer_hand + cards

    def validMove(self, card):
        """returns true if card (the card being played) is legally
        playable after move"""
        face_up = self.history[-1][1]  # the face up card to play on
        opponent_drew = self.history[-1][3] != 0  # whether the opponent drew last turn
        if (face_up in [1, 14, 27, 40] and not opponent_drew): #last play was a 2
            return card in [1, 14, 27, 40] #playing a 2 on a 2 is legal 
        elif ((card - 7) % 13 == 0):  # card is an 8, always playable
            return True
        elif (card / 13 == face_up / 13):  # cards are the same suit
            return True
        elif (card % 13 == face_up % 13):  # cards are the same value
            return True
        else:
            return False

    def executeSpecialMove(self, card):
        """ Executes special cards. Returns true if opposing player's turn is skipped """
        if (card == 11):  # card is the Queen of Spades, make opponent draw 5
            if self.currentPlayer == 0:  # if player is human
                self.history.append((0, 11, 0, 5))
            else:  # if player is ai
                self.history.append((1, 11, 0, 5))
            return True
        # elif card is number 2
        elif((card - 10) % 13 == 0):  # card is Jack, make opponent skip turn
            if self.currentPlayer == 0:
                self.history.append((0, card, self.history[-1][2], 0))
            else:
                self.history.append((1, card, self.history[-1][2], 0))
            return True
        else:
            return False

    def executeMove(self, move):
        """ Assumes player's move is valid and continues to execute the move """
        self.history.append(move)
        if self.currentPlayer == 0:
            if(move[3] == 0): #no draw, card was played
                self.human_hand.remove(move[1])
            else:
                self.draw(0, move[3])
            if(self.executeSpecialMove(move[1])):  # checks if card is a special card & execute it if it is
                self.currentPlayer = self.currentPlayer  # skip opposing player's turn
            else:
                self.currentPlayer = 1
        else:
            if(move[3] == 0): #no draw, card was played
                self.computer_hand.remove(move[1])
            else:
                self.draw(1, move[3])
            if(self.executeSpecialMove(move[1])):  # checks if card is a special card & execute it if it is
                self.currentPlayer = self.currentPlayer  # skip opposing player's turn
            else:
                self.currentPlayer = 0

    def move(self, partial_state):
        """
            Receives a partial_state that is a tuple (face_up_card, suit, hand, history)
            face_up_card = current card next move must be made on, history = [moves]
            Plays a card that is of the same suit or same number or an 8
        """
        hand = partial_state[2]
        for card in hand:
            if self.validMove(card):
                return (1, card, card / 13, 0)
        return (1, self.history[-1][1], self.history[-1][2], 1)

    def movePefectKnowedge(self, state):
        """ Receives a tuple (deck, hand, partial_state), hand represents the other player's hand """
        return

    def isGameOver(self):
        """ Checks if the game is over yet """
        return [] in [self.deck, self.human_hand, self.computer_hand]

    def getWinner(self):
        """ Assumes game is over. Gets winner of game based on hands """
        if(len(self.human_hand) < len(self.computer_hand)):
            return "Player wins!"
        elif(len(self.human_hand) > len(self.computer_hand)):
            return "Computer wins!"
        else:
            if min(self.human_hand) < min(self.computer_hand):
                return "Player wins!"
            elif min(self.computer_hand) < min(self.human_hand):
                return "Computer wins!"
            else:
                return "error"
