import random
from globals import suits, ranks
from Card import Card

class Deck:
    #Using the global module imported in this class, a deck can be created
    #It adds cards to a deck with all the types of suits and ranks available
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    #Display the deck
    def __str__(self):
        deck_composition = ''
        for card in self.deck:
            deck_composition += '\n '+card.__str__()
        return 'The deck has:' + deck_composition

    #Shuffling the deck to make a draw less predictable
    def shuffle(self):
        random.shuffle(self.deck)

    #This method returns a card from the deck, by using the pop() method
    #The pop method also removes the card from the deck so it won't be drawn again
    def deal(self):
        single_card = self.deck.pop()
        return single_card