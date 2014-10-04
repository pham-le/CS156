#!/usr/bin/python
import random

class CrazyEights:
    """Contains fuctions that can be used to run a game of Crazy Eights"""

    def get_suit(self, card):
        """returns a suit value for the card: (spades: 0, hearts: 1, diamonds: 2, clubs: 3)"""
        return card / 13

    def get_value(self, card):
        """returns the numeric value of a card"""
        return card % 13

    def get_initial_state(self, starting_player):
        """returns a tuple representing a complete game state right after hands have been
        delt, and there is 1 card face-up."""
        deck = range(52)
        random.shuffle(deck)

        #draw each hand from the deck
        human_hand = deck[-8:]
        deck = deck[:-8]
        computer_hand = deck[-8:]
        deck = deck[:-8]

        face_up_card = deck.pop()
        suit = self.get_suit(face_up_card)

        if starting_player == 0:
            history = [(1, face_up_card, suit, 0)]
            partial_state = (face_up_card, suit, human_hand, history)
            initial_state = (deck, computer_hand, partial_state)
        else:
            history = [(0, face_up_card, suit, 0)]
            partial_state = (face_up_card, suit, computer_hand, history)
            initial_state = (deck, human_hand, partial_state)
        return initial_state