from typing import List, Dict, Set
from handtypes import HandTypes
from card import Card
from deck import Deck

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
        hand_by_rank: Dict[str, List[str]] = dict.fromkeys(Card.CARD_RANKS, [])

        print(hand_by_rank)

        #for card in self._cards:
            #if card._card_rank in hand_by_rank:
                #hand_by_rank[card._card_rank] = hand_by_rank[card._card_rank].append(card._card_suit)
        
        hand_by_rank['As'].append(3)

        print(hand_by_rank)