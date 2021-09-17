import random
import handCheck


class Card:  # create a class "Card"
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    def __str__(self):
        return self.suit + str(self.value)

    def show(self):  # Form the output style. Example= "1 of Spades"
        print("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self):  # Create a list for the Deck
        self.cards = []
        self.build()

    def build(self):  # Build the Deck
        for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:  # All the possible colors
            for v in range(1, 14):
                self.cards.append(Card(s, v))  # For all the colors, create 13 numbers from 1-13.

    def show(self):  # Function to show the deck
        for c in self.cards:
            c.show()

    def shuffle(self):  # Shuffle function
        for i in range(len(self.cards) - 1, 0, -1):  # Start from back of the array. Move back to 0 in decrements of 1.
            r = random.randint(0, i)  # Pick a random number from 0 to rest of the cards to shuffle.
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]  # Swap 2 cards with the random position.

    def drawCard(self):
        return self.cards.pop()  # returns the card with index -1, or the top card from the deck.


class Player:  # Create players
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):  # Puts 5 cards in the back of the list
        for i in range(5):
            self.hand.append(deck.drawCard())
        return self

    def showHand(self):
        for card in self.hand:
            card.show()
        handCheck.score_hand(self.hand)
