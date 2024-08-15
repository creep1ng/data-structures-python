from typing import List, Dict, Set
from handtypes import HandType
from card import Card
from deck import Deck
from collections import Counter

class Hand:
    _cards: List[Card]
    _player_name: str

    def __init__(self, deck: Deck, player_name: str) -> None:
        self._cards = [deck.pick_card() for _ in range(6)]
        self._player_name = player_name

    def __repr__(self) -> str:
        return f"{self._player_name} has {self._cards}"

    def sort(self) -> None:
        """Sorts in-place the cards according to cards' rank's values."""

        # Just a wrapper of sorted ;)
        self._cards = sorted(self._cards)

    def replace(self, deck: Deck, card_index: int) -> None:
        """Replace the `card_index` with a random card. The cards' index starts in 0."""
        if card_index not in [i for i in range(1, 6)]:
            raise IndexError(f"Cannot replace the {
                             card_index}th card. Use a index between 1 and 5.")

        self._cards[card_index] = deck.pick_card()

    def __is_flush(self, suits):
        return len(set(suits)) == 1

    def __is_straight(self, values):
        sorted_values = sorted(values)
        return all(sorted_values[i] + 1 == sorted_values[i + 1] for i in range(len(sorted_values) - 1))

    def _get_hand_type(self) -> 'HandTypes':
        """To get the frequency of cards suits, we can use a dict like this:
        {
            'clubs': {A, 2},
            'spades': [2],
            'hearts': [J], 
            'diamonds': [10]
        }

        {
            'As': ['clubs'],
            'Q': [],
            'J': ['hearts'],
            ...
        }
        """

        ranks = [card._card_rank for card in self._cards]
        suits = [card._card_suit for card in self._cards]
        value_counts = Counter(ranks)
        unique_values = list(value_counts.values())

        is_flush = self.__is_flush(suits)
        is_straight = self.__is_straight(ranks)

        
        # Check for Royal Flush
        if is_flush and sorted(ranks) == [10, 11, 12, 13, 14]:
            return HandType.ROYAL_FLUSH

        # Check for Straight Flush
        if is_flush and is_straight:
            return HandType.STRAIGHT_FLUSH

        # Check for Four of a Kind
        if 4 in unique_values:
            return HandType.FOUR_OF_A_KIND

        # Check for Full House
        if 3 in unique_values and 2 in unique_values:
            return HandType.FULL_HOUSE

        # Check for Flush
        if is_flush:
            return HandType.FLUSH

        # Check for Straight
        if is_straight:
            return HandType.STRAIGHT

        # Check for Three of a Kind
        if 3 in unique_values:
            return HandType.THREE_OF_A_KIND

        # Check for Two Pair
        if unique_values.count(2) == 2:
            return HandType.TWO_PAIR

        # Check for One Pair
        if 2 in unique_values:
            return HandType.ONE_PAIR

        return HandType.HIGH_CARD
