from hand import Hand
from deck import Deck

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

    print(p1._get_hand_type())