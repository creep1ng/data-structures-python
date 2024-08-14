from typing import List
from random import choice
from card import Card

class Deck:
    _CARDS: List[Card] = [Card(card_rank, card_suit)
                          for card_suit in Card.CARD_SUITS.keys() for card_rank in Card.CARD_RANKS]

    _cards: List[Card]

    def __init__(self) -> None:
        # Initializing a shuffled _CARDS. The shuffle is random and changes on each execution.
        self._cards = sample(self._CARDS, k=len(self._CARDS))

    def __repr__(self) -> str:
        return f"{self._cards}"

    def pick_card(self) -> Card:
        """Pick a random card from the deck, removes this card from the deck, and return the picked card."""
        picked_card = choice(self._cards)
        self._cards.remove(picked_card)

        return picked_card

