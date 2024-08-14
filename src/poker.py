from typing import List, Dict
from random import sample, choice
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

    def _get_hand_type(self) -> 'HandTypes':
        """To get the frequency of cards suits, we can use a dict like this:
        {
            'clubs': [A, 2],
            'spades': [2],
            'hearts': [J], 
            'diamonds': [10]
        }
        """

        hand_by_suit: Dict[str, List[str]] = dict.fromkeys(Card.CARD_SUITS, [])

        for card in self._cards:
            hand_by_suit[card._card_suit].append(card._card_rank)

        


class HandTypes(Enum):
    HIGH_CARD = auto()
    ONE_PAIR = auto()
    # ...


if __name__ == "__main__":
    deck = Deck()
    print(deck._CARDS)
    p1 = Hand(deck, "p1")
    print("*"*30)
    print()

    print(p1)
    print(deck._cards)
    print("*"*30)
    print()

    p1.replace(deck, 2)
    print(p1)
    print(deck)
    print("*"*30)

    print(p1.sort())
