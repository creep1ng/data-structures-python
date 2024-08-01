from typing import List, Dict
from random import sample

class Card:
    #CARD_RANKS stores the possible values for each card rank.
    CARD_RANKS: List[str] = ["As", "2", "3", "4,", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    #CARD_SUITS stores the possible values for each card suit.
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
        `card_rank`: Must be one of "As", "2", "3", "4,", "5", "6", "7", "8", "9", "10", "J", "Q", "K".
        `card_suit: Must be one of "clubs", "diamonds", "hearts", or "spades".capitalize

        Raises ValueError if `card_rank` and/or `card_suit` isn't one of the accepted values.
        """

        if card_rank not in self.CARD_RANKS:
            raise ValueError(f"`card_rank` must be some of these options: {CARD_RANKS}")

        if card_suit not in self.CARD_SUITS.keys():
            raise ValueError(f"`card_suit` must be some of these options: {self.CARD_SUITS.keys()}")

        self._card_rank = card_rank
        self._card_suit = card_suit

    def __repr__(self) -> str:
        return f"{self.CARD_SUITS[self._card_suit]}{self._card_rank}"

class Deck:
    _CARDS: List[Card] = [Card(card_rank, card_suit) for card_suit in Card.CARD_SUITS.keys() for card_rank in Card.CARD_RANKS]
    
    _cards: List[Card]

    def __init__(self) -> None:
        self._cards = sample(self._CARDS, k=len(self._CARDS))

    def __repr__(self) -> str:
        return f"{[card.__repr__ for card in self._cards]}"

if __name__ == "__main__":
    c1 = Card("As", "clubs")
    print(c1)
    print(Deck._CARDS)
    print(Deck()._cards)
