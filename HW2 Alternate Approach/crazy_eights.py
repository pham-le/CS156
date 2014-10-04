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
        #state = (deck, other_hand, partial_state)
        #move = (player_num, face_up_card, suit, number_of_cards)
        #partial_state = (face_up_card, suit, our_hand, history)
        if move[3] == 0: #player did not draw any cards
            other_hand = state[2][2]
            partial_state = (move[1], move[2], state[1].remove(move[1]), state[2].append(move))
            state = (state[0], other_hand, partial_state)
        elif move[3] > len(state[0]): #if num of cards drawn is larger than the amount in the deck
            cards = state[0][-1 * len(state[0]):]
            deck = []
            other_hand = state[2][2]
            partial_state = (move[1], move[2], state[1]+cards, state[2].append(move))
            state = (deck, other_hand, partial_state)
        else: #if player draws appropriate amount
            cards = state[0][-1 * move[3]:]
            deck = state[0][:-1 * move[3]]
            other_hand = state[2][2]
            partial_state = (move[1], move[2], state[1]+cards, state[2].append(move))
            state = (deck, other_hand, partial_state)
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