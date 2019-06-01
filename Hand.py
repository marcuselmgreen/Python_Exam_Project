from globals import ranks, values

class Hand:
    def __init__(self):
        #Cards in hand
        self.cards = []
        #Total value of cards
        self.value = 0

    #Method that adds a card to the hand and updates the total value
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

    #When an ace is drawn in BlackJack it can either have a value of 1 or 11
    #This method checks if the hand value exceeds 21 and reduces the ace value to 1
    #The ace card is given a true or false value, so it won't reduce the same card twice
    def check_ace(self):
        ace = 'Ace'
        for card in self.cards:
            if card.rank == ace and self.value > 21 and card.check == False:
                self.value -= 10
                card.check = True
                print("\nReduced value of %s from 11 to 1" % (card))
