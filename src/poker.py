from typing import List, Dict

class Card:
    #_CARD_RANKS stores the possible values for each card rank.
    _CARD_RANKS: List[str] = ["As", "2", "3", "4,", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    #_CARD_SUITS stores the possible values for each card suit.
    _CARD_SUITS: Dict[str, str] = {
        "clubs": "♣",
        "diamonds": "♦",
        "hearts": "♥",
        "spades": "♠"
    }

    _card_rank: str
    _card_suit: str

    def __init__(self, card_rank, card_suit) -> None:
        if card_rank not in self._CARD_RANKS:
            raise ValueError(f"`card_rank` must be some of these options: {_CARD_RANKS}")

        if card_suit not in self._CARD_SUITS.keys():
            raise ValueError(f"`card_suit` must be some of these options: {self._CARD_SUITS.keys()}")

        self._card_rank = card_rank
        self._card_suit = card_suit

    def __repr__(self) -> str:
        return f"{self._CARD_SUITS[self._card_suit]}{self._card_rank}"

if __name__ == "__main__":
    c1 = Card("As", "clubs")
    print(c1)
