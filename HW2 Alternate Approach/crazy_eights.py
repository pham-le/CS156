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

        # draw each hand from the deck
        human_hand = deck[-8:]
        deck = deck[:-8]
        computer_hand = deck[-8:]
        deck = deck[:-8]

        face_up_card = deck.pop()
        suit = self.get_suit(face_up_card)

        if starting_player is 0:
            history = [(1, face_up_card, suit, 0)]
            partial_state = (face_up_card, suit, human_hand, history)
            initial_state = (deck, computer_hand, partial_state)
        else:
            history = [(0, face_up_card, suit, 0)]
            partial_state = (face_up_card, suit, computer_hand, history)
            initial_state = (deck, human_hand, partial_state)
        return initial_state

    def actions(self, partial_state):
        """returns the set of moves that are playable in the state."""
        face_up_card, face_up_suit, hand, history = partial_state
        face_up_value = self.get_value(face_up_card)
        player = 0 if (history[-1][0] is 1) else 1 #the player who must play next 
        actions = []
        if len(history) > 1:  # special cards only apply past turn 1
            if history[-1][3] is 0:  # opponent didn't draw, so their special cards apply
                if face_up_card is 11:  #queen of spades, can only draw 5
                    actions.append((player, face_up_card, face_up_suit, 5))
                    return actions
                if face_up_value is 1:  #2 is face-up
                    for card in hand:
                        if self.get_value(card) is face_up_value:  #you have a 2
                            actions.append((player, card, self.get_suit(card), 0))
                    two_counter = 1  #keep track of how much you must draw
                    while (two_counter < 5
                           and len(history) > (two_counter + 1)  #don't want to check first faceup card
                           and self.get_value(history[-(two_counter + 1)][1]) is 1):  #previous card is 2
                        two_counter = two_counter + 1
                    actions.append((player, face_up_card, face_up_suit, 2 * two_counter))
                    return actions
                if (face_up_value is 10) and (
                            history[-2][1] != face_up_card):  #jack face up, and opponent wasn't skipped
                    return actions  #you can't play any moves
        for card in hand:
            if self.get_value(card) is 7:
                for i in range(4):
                    actions.append((player, card, i, 0))
            elif (self.get_suit(card) is face_up_suit
                  or self.get_value(card) is face_up_value):
                actions.append((player, card, self.get_suit(card), 0))
        actions.append((player, face_up_card, face_up_suit, 1))
        return actions

    def result(self, state, move):
        """returns the resulting state after move has been applied to it"""
        deck, other_hand, partial_state = state
        face_up_card, face_up_suit, our_hand, history = partial_state
        player_moved, played_card, played_suit, drawn_cards = move

        if move is None:
            return state
        elif drawn_cards is 0:  # player did not draw any cards
            our_hand.remove(played_card)
            history.append(move)
            partial_state = (played_card, played_suit, other_hand, history)
            state = (deck, our_hand, partial_state)
        else:  # player drew cards
            if drawn_cards > len(deck):  # player drew more cards than in deck
                drawn_cards = len(deck)
            our_hand = our_hand + deck[-1 * drawn_cards:]
            deck = deck[:-1 * drawn_cards]
            history.append(move)
            partial_state = (played_card, played_suit, other_hand, history)
            state = (deck, our_hand, partial_state)
        return state


    def game_over(self, state):
        """returns true if the game is over in this state"""
        # check if deck, opponent hand, or your hand is empty
        deck, human_hand, partial_state = state
        computer_hand = partial_state[2]
        return [] in [deck, computer_hand, human_hand]

    def utility(self, state, player):
        return 0

    def move_perfect_knowledge(self, state):
        """Picks a move based on the state and the minimax algorithm with
        alpha-beta pruning and the limiting hueristic: hand - opponent hand"""
        actions = self.actions(state[2])
        if actions is []:
            return None
        return self.actions(state[2])[0]
