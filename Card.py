class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.check = False

    #Display the cards
    def __str__(self):
        return "%s of %s" % (self.rank, self.suit)

    #When concatenating a string and a card
    def __radd__(self, other):
        return other + str(self)