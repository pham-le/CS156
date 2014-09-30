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
        self.player_one_hand = self.draw(8)  # draws 8 cards for player 1
        self.player_two_hand = self.draw(8)  # draws 8 cards for player 2
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

    def draw(self, numCards):
    	""" Helper function to draw x number of cards from the deck"""
        cards = self.deck[-1 * numCards:]
        self.deck = self.deck[:-1 * numCards]
        return cards

    def appendHistory(self, move):
        """
            History appends a move that is a quadruple (player_num, face_up_card, suit, number_of_cards)
            faceupcard = card after the move, suit = next suit that must be played, numofcards = num of cards player picked up if any
        """
        self.history.append(move)

    def validMove(self, card):
        """returns true if card (the card being played) is legally
        playable after move"""
        face_up = self.history[-1][1]  # the face up card on to play on
        if ((card - 1) % 13 == 0):  # card is an 2, always playable
            return True
        elif ((card - 7) % 13 == 0):  # card is an 8, always playable
            return True
        elif ((card - 10) % 13 == 0):  # card is an Jack, always playable
            return True
        elif (card == 11):  # card is the Queen of Spades, always playable
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
            if(self.currentPlayer == 0):  # if player is human
                self.player_two_hand = self.player_two_hand + self.draw(5)  # make ai draw
                return True
            else:  # if player is ai
                self.player_one_hand = self.player_one_hand + self.draw(5)  # make human draw
                return True
        # elif card is number 2
        elif((card - 10) % 13 == 0):  # card is Jack, make opponent skip turn
            return True
        else:
            return False

    def executeMove(self, move):
        """ Assumes player's move is valid and continues to execute the move """
        self.appendHistory(move)
        if (self.currentPlayer == 0):
            self.player_one_hand.remove(move[1])
            if(self.executeSpecialMove(move[1])):  # checks if card is a special card & execute it if it is
                self.currentPlayer = self.currentPlayer  # skip opposing player's turn
            else:
                self.currentPlayer = 1
        else:
            self.player_two_hand.remove(move[1])
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
        checksPlayerHand = False
        for card in self.player_one_hand:
            if(self.validMove(card)):
                checksPlayerHand = True

        checksComputerHand = False
        for card in self.player_one_hand:
            if(self.validMove(card)):
                checksComputerHand = True

        return (len(self.deck) > 0) and checksComputerHand and checksPlayerHand

    def getWinner(self):
        """ Assumes game is over. Gets winner of game based on hands """
        if(len(self.player_one_hand) < len(self.player_two_hand)):
            return "Player wins!"
        elif(len(self.player_one_hand) > len(self.player_two_hand)):
            return "Computer wins!"
        else:
            playerMin = self.player_one_hand[0]
            for card in self.player_one_hand:
                if card < playerMin:
                    playerMin = card

            computerMin = self.player_two_hand[0]
            for card in self.player_two_hand:
                if card < computerMin:
                    computerMin = card
            if playerMin < computerMin:
                return "Player wins!"
            elif computerMin < playerMin:
                return "Computer wins!"
            else:
                return "error"
