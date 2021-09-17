from Deck import *


def play():
    deck = Deck()
    deck.shuffle()
    jaakko = Player("Jaakko")
    niklas = Player("Niklas")
    napoleon = Player("Napoleon")

    print("Jaakko's hand:")
    jaakko.draw(deck)
    jaakko.showHand()

    print("Niklas's hand:")
    niklas.draw(deck)
    niklas.showHand()

    print("Napoleon's hand:")
    napoleon.draw(deck)
    napoleon.showHand()
play()

