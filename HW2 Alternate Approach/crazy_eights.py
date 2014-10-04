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

    def actions(self, partial_state):
        """returns the set of moves that are playable in the state"""
        return []

    def result(self, state, move):
        """returns the resulting state after move has been applied to it"""
        return state

    def game_over(self, state):
        """returns true if the game is over in this state"""
        #check if deck, opponent hand, or your hand is empty
        return [] in [state[0], state[1], state[2][2]]

    def utility(self, state, player):
        return 0

    def move_perfect_knowledge(state):
        """Picks a move based on the state and the minimax algorithm with
        alpha-beta pruning and the limiting hueristic: hand - opponent hand"""
        return state



#comment        