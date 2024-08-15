from typing import List, Dict, Set
from handtypes import HandType
from card import Card
from deck import Deck
from collections import Counter

class Hand:
    _cards: List[Card]
    _player_name: str

    def __init__(self, deck: Deck, player_name: str) -> None:
        self._cards: List[Card] = [deck.pick_card() for _ in range(6)]
        self._player_name: str = player_name

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

    def __is_flush(self, suits: List[str]):
        return len(set(suits)) == 1

    def __is_straight(self, values: List[str]):
        sorted_values = sorted(values)
        return all(sorted_values[i] + 1 == sorted_values[i + 1] for i in range(len(sorted_values) - 1))

    
    def _get_hand_type(self) -> HandType:
        ranks = [card._card_rank for card in self._cards]
        suits = [card._card_suit for card in self._cards]
        
        values = [Card.CARD_RANKS.index(rank) for rank in ranks]
        values.sort()
        
        is_flush = self.__is_flush(suits)
        is_straight = self.__is_straight(values)

        rank_counts = Counter(values)
        most_common = rank_counts.most_common()
        
        # Check for Royal Flush
        if is_flush and values == [8, 9, 10, 11, 12]:
            return HandType.ROYAL_FLUSH
        # Check for Straight Flush
        if is_flush and is_straight:
            return HandType.STRAIGHT_FLUSH
        # Check for Four of a Kind
        if most_common[0][1] == 4:
            return HandType.FOUR_OF_A_KIND
        # Check for Full House
        if most_common[0][1] == 3 and most_common[1][1] == 2:
            return HandType.FULL_HOUSE
        # Check for Flush
        if is_flush:
            return HandType.FLUSH
        # Check for Straight
        if is_straight:
            return HandType.STRAIGHT
        # Check for Three of a Kind
        if most_common[0][1] == 3:
            return HandType.THREE_OF_A_KIND
        # Check for Two Pair
        if most_common[0][1] == 2 and most_common[1][1] == 2:
            return HandType.TWO_PAIR
        # Check for One Pair
        if most_common[0][1] == 2:
            return HandType.ONE_PAIR
        # Else, return High Card
        return HandType.HIGH_CARD
    
    def __str__(self) -> str:
        """Retorna una representación en cadena de la mano del jugador."""
        return f"Hand of {self._player_name}: " + ", ".join([str(card) for card in self._cards])
    
    def __eq__(self, other) -> bool:
        """Compara si dos manos son iguales basado en el tipo de mano."""
        if isinstance(other, Hand):
            return self._get_hand_type() == other._get_hand_type()
        return False