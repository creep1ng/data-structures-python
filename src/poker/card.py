from typing import List, Dict
from enum import Enum, auto

class Card:
    # CARD_RANKS stores the possible values for each card rank.
    # The ranks are sorted from smallest value to highest value.
    CARD_RANKS: List[str] = ["2", "3", "4",
                             "5", "6", "7", "8", "9", "10", "J", "Q", "K", "As"]

    # CARD_SUITS stores the possible values for each card suit.
    CARD_SUITS: Dict[str, str] = {
        "clubs": "♣",
        "diamonds": "♦",
        "hearts": "♥",
        "spades": "♠"
    }

    _card_rank: str
    _card_suit: str

    def __init__(self, card_rank: str, card_suit: str) -> None:
        """Creates an instance of `Card`.
        `card_rank`: Must be one of "2", "3", "4,", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "As".
        `card_suit: Must be one of "clubs", "diamonds", "hearts", or "spades".capitalize

        Raises ValueError if `card_rank` and/or `card_suit` isn't one of the accepted values.
        """

        if card_rank not in self.CARD_RANKS:
            raise ValueError(
                f"`card_rank` must be some of these options: {CARD_RANKS}")

        if card_suit not in self.CARD_SUITS.keys():
            raise ValueError(f"`card_suit` must be some of these options: {
                             self.CARD_SUITS.keys()}")

        self._card_rank = card_rank
        self._card_suit = card_suit

    def __repr__(self) -> str:
        return f"{self.CARD_SUITS[self._card_suit]}{self._card_rank}"

    def __gt__(self, y) -> bool:
        return self.CARD_RANKS.index(self._card_rank) <= self.CARD_RANKS.index(y._card_rank)
    
    def __str__(self) -> str:
        """Retorna una representación en cadena de la carta."""
        return f"{self.CARD_RANKS[self.CARD_RANKS.index(self._card_rank)]} de {self._card_suit.capitalize()}"
    
    