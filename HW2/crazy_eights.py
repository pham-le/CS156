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
        if numCards > len(self.deck):
            numCards = len(self.deck)
        cards = self.deck[-1 * numCards:]
        self.deck = self.deck[:-1 * numCards]
        if playernum == 0:
            self.human_hand = self.human_hand + cards
        else:
            self.computer_hand = self.computer_hand + cards

    def validMove(self, move):
        """returns true if card (the card being played) is legally
        playable after move"""
        card = move[1]
        face_up = self.history[-1][1]  # the face up card to play on
        suit = face_up/13 #the suit to play on
        if (move[3] == 0 and #trying to play
                ((self.currentPlayer == 0 and card not in self.human_hand) or
                (self.currentPlayer == 1 and card not in self.computer_hand))):
            print "INVALID: Card is not in your hand!"
            return False
        if face_up in [7, 20, 33, 46]:  #8 face-up, reset suit
            suit = self.history[-1][2]
        opponent_drew = self.history[-1][3] != 0  #whether the opponent drew last turn
        if ((len(self.history) > 1) #not first turn
                and (face_up in [1, 14, 27, 40]) #face-up 2
                and (not opponent_drew) #opponent didn't draw
                and (card not in [1, 14, 27, 40]) #you're not playing a 2
                and (move[3] == 0)): #you're trying to not draw
            print "INVALID: You must play a 2 or draw"
            return False
        elif (card in [7, 20, 33, 46]): #8 always valid at this point
            return True 
        elif ((card / 13 !=  suit) 
                and (card % 13 != face_up % 13)):  #cards don't match suit or value
            print "INVALID: Either suit or value must match the face-up card"
            return False
        else:
            return True

    def executeSpecialMove(self, card):
        """ Executes special cards."""
        if (card == 11):  # card is the Queen of Spades, make opponent draw 5
            if self.currentPlayer == 0:  # if player is human
                self.history.append((1, card, 0, 5))
                self.draw(1, 5)
            else:  # if player is ai
                self.history.append((0, card, 0, 5))
                self.draw(0, 5)
        # elif card in [1, 14, 27, 40]: #card is 2
        #     if self.currentPlayer == 0:  # if player is human
        #         self.history.append((1, card, card/13, 2))
        #         self.draw(1, 2)
        #     else:  # if player is ai
        #         self.history.append((0, card, card/13, 2))
        #         self.draw(0, 2)
        elif card in [10, 23, 36, 49]:  # card is Jack, make opponent skip turn
            if self.currentPlayer == 0:
                self.history.append((1, card, card/13, 0))
            else:
                self.history.append((0, card, card/13, 0))
        else:
            if self.currentPlayer == 0:
                self.currentPlayer = 1
            else:
                self.currentPlayer = 0

    def executeMove(self, move):
        """ Assumes player's move is valid and continues to execute the move """
        self.history.append(move)
        if self.currentPlayer == 0:
            if(move[3] == 0): #no draw; card was played
                self.human_hand.remove(move[1])
                self.executeSpecialMove(move[1])
            else:
                self.draw(0, move[3])
                self.currentPlayer = 1
        else:
            if(move[3] == 0): #no draw; card was played
                self.computer_hand.remove(move[1])
                self.executeSpecialMove(move[1])
            else:
                self.draw(1, move[3])
                self.currentPlayer = 0

    def move(self, partial_state):
        """
            Receives a partial_state that is a tuple (face_up_card, suit, hand, history)
            face_up_card = current card next move must be made on, history = [moves]
            Plays a card that is of the same suit or same number or an 8
        """
        hand = partial_state[2]
        for card in hand:
            move = (1, card, card / 13, 0)
            if self.validMove(move):
                return move
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
