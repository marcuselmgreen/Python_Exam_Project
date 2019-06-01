class Chips:
    def __init__(self):
        self.total = 0
        self.bet = 0

    #A normal win increases the total amount of chips by the size of the bet
    def win(self):
        self.total += self.bet

    #A BlackJack win increases the total amount of chips by 1.5 times the bet
    def bj_win(self):
        self.total += (self.bet * 1.5)

    def loss(self):
        self.total -= self.bet


