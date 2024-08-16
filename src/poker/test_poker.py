from unittest import TestCase
from .card import Card
from .deck import Deck
from .hand import Hand
from .handtypes import HandType

class TestHand(TestCase):
    
    def setUp(self):
        """Set up a deck and player name for each test."""
        self.deck = Deck()
        self.player_name = "Player 1"

    def test_royal_flush(self):
        """Test if a Royal Flush is correctly identified."""
        cards = [
            Card('10', 'spades'), Card('J', 'spades'), 
            Card('Q', 'spades'), Card('K', 'spades'), 
            Card('As', 'spades')
        ]
        hand = Hand(deck=None, player_name=self.player_name)
        hand._cards = cards
        
        self.assertEqual(hand._get_hand_type(), HandType.ROYAL_FLUSH)

    def test_straight_flush(self):
        """Test if a Straight Flush is correctly identified."""
        cards = [
            Card('7', 'hearts'), Card('8', 'hearts'), 
            Card('9', 'hearts'), Card('10', 'hearts'), 
            Card('J', 'hearts')
        ]
        hand = Hand(deck=None, player_name=self.player_name)
        hand._cards = cards
        
        self.assertEqual(hand._get_hand_type(), HandType.STRAIGHT_FLUSH)

    def test_four_of_a_kind(self):
        """Test if Four of a Kind is correctly identified."""
        cards = [
            Card('9', 'clubs'), Card('9', 'diamonds'), 
            Card('9', 'hearts'), Card('9', 'spades'), 
            Card('2', 'hearts')
        ]
        hand = Hand(deck=None, player_name=self.player_name)
        hand._cards = cards
        
        self.assertEqual(hand._get_hand_type(), HandType.FOUR_OF_A_KIND)

    def test_full_house(self):
        """Test if Full House is correctly identified."""
        cards = [
            Card('J', 'clubs'), Card('J', 'diamonds'), 
            Card('J', 'hearts'), Card('2', 'spades'), 
            Card('2', 'hearts')
        ]
        hand = Hand(deck=None, player_name=self.player_name)
        hand._cards = cards
        
        self.assertEqual(hand._get_hand_type(), HandType.FULL_HOUSE)

    def test_flush(self):
        """Test if a Flush is correctly identified."""
        cards = [
            Card('2', 'diamonds'), Card('6', 'diamonds'), 
            Card('9', 'diamonds'), Card('J', 'diamonds'), 
            Card('K', 'diamonds')
        ]
        hand = Hand(deck=None, player_name=self.player_name)
        hand._cards = cards
        
        self.assertEqual(hand._get_hand_type(), HandType.FLUSH)

    def test_straight(self):
        """Test if a Straight is correctly identified."""
        cards = [
            Card('3', 'hearts'), Card('4', 'diamonds'), 
            Card('5', 'clubs'), Card('6', 'spades'), 
            Card('7', 'hearts')
        ]
        hand = Hand(deck=None, player_name=self.player_name)
        hand._cards = cards
        
        self.assertEqual(hand._get_hand_type(), HandType.STRAIGHT)

    def test_three_of_a_kind(self):
        """Test if Three of a Kind is correctly identified."""
        cards = [
            Card('4', 'clubs'), Card('4', 'diamonds'), 
            Card('4', 'hearts'), Card('K', 'spades'), 
            Card('2', 'hearts')
        ]
        hand = Hand(deck=None, player_name=self.player_name)
        hand._cards = cards
        
        self.assertEqual(hand._get_hand_type(), HandType.THREE_OF_A_KIND)

    def test_two_pair(self):
        """Test if Two Pair is correctly identified."""
        cards = [
            Card('5', 'clubs'), Card('5', 'diamonds'), 
            Card('J', 'hearts'), Card('J', 'spades'), 
            Card('3', 'hearts')
        ]
        hand = Hand(deck=None, player_name=self.player_name)
        hand._cards = cards
        
        self.assertEqual(hand._get_hand_type(), HandType.TWO_PAIR)

    def test_one_pair(self):
        """Test if One Pair is correctly identified."""
        cards = [
            Card('8', 'clubs'), Card('8', 'diamonds'), 
            Card('3', 'hearts'), Card('K', 'spades'), 
            Card('2', 'hearts')
        ]
        hand = Hand(deck=None, player_name=self.player_name)
        hand._cards = cards
        
        self.assertEqual(hand._get_hand_type(), HandType.ONE_PAIR)

    def test_high_card(self):
        """Test if High Card is correctly identified."""
        cards = [
            Card('2', 'clubs'), Card('4', 'diamonds'), 
            Card('8', 'hearts'), Card('J', 'spades'), 
            Card('K', 'hearts')
        ]
        hand = Hand(deck=None, player_name=self.player_name)
        hand._cards = cards
        
        self.assertEqual(hand._get_hand_type(), HandType.HIGH_CARD)


if __name__ == "__main__":
    TestHand.main()