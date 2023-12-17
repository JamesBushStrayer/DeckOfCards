# Week 8 - Deck of Cards Lab
# CIS 261
# James Alan Bush (SU200619708)


import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.deck = [Card(rank, suit) for suit in suits for rank in ranks]

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, number_of_cards):
        return [self.deck.pop() for _ in range(min(number_of_cards, len(self.deck)))]

    def count(self):
        return len(self.deck)

def main():
    deck = Deck()
    deck.shuffle()
    print("Card Dealer")
    print("I have shuffled a deck of 52 cards.")

    number_of_cards = int(input("How many cards would you like?: "))

    cards = deck.deal(number_of_cards)
    print("\nHere are your cards:")
    for card in cards:
        print(card)

    print(f"\nThere are {deck.count()} cards left in the deck.")
    print("\nGood luck!")

if __name__ == "__main__":
    main()
