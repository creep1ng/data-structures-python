from unittest import TestCase
from src.poker.card import Card
from src.poker.deck import Deck
from src.poker.hand import Hand
from src.poker.handtypes import HandTypes

class TestPoker(TestCase):
    
    def test_pick_card(self) -> None:
        deck: Deck = Deck()
        hand: Hand = Hand(deck, "test")
        hand.pick_card()