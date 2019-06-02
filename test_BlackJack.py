import unittest
from Hand import Hand
from Card import Card
from Deck import Deck
from Chips import Chips

#Run - python -m unittest test_BlackJack.py

class TestHand(unittest.TestCase):
    #Reduce ace after getting a value > 21
    def test_ace_reduction(self):
        hand = Hand()
        hand.add_card(Card('Spades', 'Seven'))        
        hand.add_card(Card('Diamonds', 'Ace'))
        hand.add_card(Card('Hearts', 'Ten'))
        hand.check_ace()
        value = hand.value
        self.assertEqual(value, 18)

    #Reduce ace value to one and don't reduce anymore after being dealt a new card
    def test_ace_reduction_only_once(self):
        hand = Hand()
        hand.add_card(Card('Spades', 'Seven'))        
        hand.add_card(Card('Hearts', 'Ten'))
        hand.add_card(Card('Diamonds', 'Ace'))
        hand.add_card(Card('Diamonds', 'Five'))
        hand.check_ace()
        value = hand.value
        self.assertEqual(value, 23)
    
    #Check if reducing value of only one ace if two ace's are the first two cards
    def test_double_ace(self):
        hand = Hand()
        hand.add_card(Card('Diamonds', 'Ace'))
        hand.add_card(Card('Hearts', 'Ace'))
        hand.check_ace()
        value = hand.value
        self.assertEqual(value, 12)

class TestDeck(unittest.TestCase):
    #Check if deck consists of 52 cards
    def test_deck_card_amount(self):
        deck = Deck()
        self.assertEqual(len(deck.deck), 52)

class TestChips(unittest.TestCase):
    #Test chips if winning normally
    def test_win(self):
        chips = Chips()
        chips.total = 1000
        chips.bet = 10
        chips.win()
        self.assertEqual(chips.total, 1010)
    
    #Test chips if losing
    def test_loss(self):
        chips = Chips()
        chips.total = 1000
        chips.bet = 10
        chips.loss()
        self.assertEqual(chips.total, 990)
    
    #Test chips if winning with blackjack
    def test_bj_win(self):
        chips = Chips()
        chips.total = 1000
        chips.bet = 10
        chips.bj_win()
        self.assertEqual(chips.total, 1015)

class TestCard(unittest.TestCase):
    #Test if a card can concatenate with string
    def test_str_and_card(self):
        card = Card('Diamonds', 'Ace')
        self.assertEqual("**Hidden Card**, " + card, "**Hidden Card**, Ace of Diamonds")

if __name__ == "__main__":
    unittest.main()