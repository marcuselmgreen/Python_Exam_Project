import random, time
from simple_colors import *
from Deck import Deck
from Card import Card
from Hand import Hand
from Chips import Chips

#This module is where the game logic is defined
#These global values are given so it can be accessed anywhere in this module
#This way winnings won't be reset everytime the player wants to initiate a new game
surrender = False
double_down = False
splitCount = 0
playing = True
winnings = 1000

def make_bet(chips):
    #Show total amount of chips
    print("\nYour chips: %s" % (winnings))
    while True:
        #User makes bet input
        bet = input(yellow('\nWhat is your bet? '))
        #Checking if input is a number and don't exceed the amount of chips available
        if not bet.isdigit():
            print(red('Bet must be a number...'))
        elif int(bet) > winnings:
            print(red('Your bet is too large...'))
        else:
            chips.bet = int(bet)
            break

#Add card to hand from deck
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.check_ace()

#This method presents all the available options to the player
def hit_or_stand(deck, hand, chips):
    global playing
    global double_down
    global surrender
    while True:
        choice = input(yellow("\nWould you like to hit or stand?\n1. Hit\n2. Stand\n3. Double Down\n4. Surrender\n"))
        #Hit
        if choice == '1':
            hit(deck, hand)
        #Stand
        elif choice == '2':
            print('\n\nPlayer is standing. Dealer is now playing...\n\n')
            #When playing is given a false value the dealer will take over
            playing = False
        #Double down
        elif choice == '3':
            #Checking if the player has enough available chips to double down
            if chips.bet * 2 < winnings:
                print("\n\nPlayer is doubling down. Increasing the bet...")
                hit(deck, hand)
                double_down = True
                playing = False
            elif chips.bet * 2 > winnings:
                print(red("\nYou don't have the chips available to double down"))
                pass
        #Surrender
        elif choice == '4':
            print(red("\n\nPlayer is surrendering."))
            #When surrender is given a true, the player bet will be halved
            surrender = True
            playing = False
        else:
            print(red('Wrong input. Try again!\n\n'))
            continue
        break

#Method that displays all cards on the table, except the first card in the dealers hand
def show_some_cards(player, dealer):
    time.sleep(1)
    #Dealer cards
    print("\n*****************")
    print("* Dealer's hand *")
    print("*****************")
    #Print everything other than the first card, seperated be comma
    print("\n--> **HIDDEN CARD**, " + dealer.cards[1], *dealer.cards[2:], sep=(', '))
    time.sleep(1)
    #Player cards
    print("\n*****************")
    print("* Player's hand *")
    print("*****************")
    #Print all the cards in the players hand
    print("\n--> " + player.cards[0], *player.cards[1:], sep=(', '))
    time.sleep(1)

#When the game is over, all the cards on the table will be displayed
def show_all_cards(player, dealer):
    time.sleep(1)
    #Dealer cards
    print("\n*****************")
    print("* Dealer's hand *")
    print("*****************")
    print("\n--> " + dealer.cards[0], *dealer.cards[1:], sep=(', '))
    #Player cards
    print("\n*****************")
    print("* Player's hand *")
    print("*****************")
    print("\n--> " + player.cards[0], *player.cards[1:], sep=(', '))

#Winning scenarios, the amount of winning chips will be increased or retracted

#Player bust
def player_bust(player, dealer, chips):
    print(red("\n*** Player busts ***"))
    chips.loss()

#Dealer bust
def dealer_bust(player, dealer, chips):
    print(green("\n*** Dealer busts ***"))
    chips.win()

#Player normal win
def player_wins(player, dealer, chips):
    print(green("\n*** Player wins ***"))
    chips.win()

#Dealer normal win
def dealer_wins(player, dealer, chips):
    print(red("\n*** Dealer wins ***"))
    chips.loss()

#Player BlackJack win
def player_wins_bj(player, dealer, chips):
    print(green("\n*** Player wins ***"))
    chips.bj_win()

#Player and dealer tie
def push(player, dealer):
    print("\n*** Player and Dealer tie ***")

#The game
while True:
    #Welcome + how to play the game intro
    print("************************")
    print("* Welcome to BlackJack *")
    print("************************")
    time.sleep(1)
    print("\n--> How to play <--")
    time.sleep(1)
    print("* Reach a final score greater than the dealer without exceeding 21 points")
    print("* Bust: the final score exceeds 21 points and the bet is lost")
    print("* BlackJack: 21 points is achieved with the first two cards")
    print("* Push: Dealer and Player finish with the same amount of points. The bet is returned")
    print("* Hit: A new card is dealt")
    print("* Stand: A new card is not dealt")
    
    #Setup deck
    deck = Deck()
    deck.shuffle()

    #Deal the first two player cards
    player_hand = Hand()
    player_hand.add_card(Card('Diamonds', 'Eight'))
    player_hand.add_card(Card('Hearts', 'Eight'))
    #player_hand.add_card(deck.deal())
    #player_hand.add_card(deck.deal())

    #Deal the first two dealer cards
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    #Setup chips
    player_chips = Chips()

    #Make bet
    make_bet(player_chips)

    #Show first cards
    show_some_cards(player_hand, dealer_hand)

    #Insurance option
    #If the dealer's upcard is an ace, the player is given an option to receive insurance
    #This way if the dealer has a BlackJack, the bet is halved
    if dealer_hand.cards[1].rank == "Ace":
        while True:
            choice = input(yellow("\nThe dealer's upcard is an ace, would you like insurance in case the dealer gets a blackjack?\n1. Yes\n2. No\n"))
            if choice == '1':
                player_chips.bet += (player_chips.bet / 2)
            elif choice == '2':
                pass
            else:
                print(red('Wrong input. Try again!\n\n'))
                continue
            break

    if player_hand.cards[0].rank == player_hand.cards[1].rank:
        while True:
            choice = input(yellow("\nThe first two cards you were dealt is the same value. Would you like to split them?\n1. Yes\n2. No\n"))
            if choice == '1':
                player_chips.bet += (player_chips.bet * 2)
                splitCount += 1
                #Make new hand
                #player_hand = Hand()
                #Add cards to each hand
            elif choice == '2':
                pass
            else:
                print(red('Wrong input. Try again!\n\n'))
                continue
            break

    #When playing is True the player is the active player
    #When False the dealer takes over, or someone hit BlackJack, or player has busted or surrendered
    while playing:
        #Break as soon as someone hits blackjack or over 21 points
        if player_hand.value == 21:
            break

        elif dealer_hand.value == 21:
            break

        #Player busts if above 21 points, and if the first two cards are not ace's
        elif player_hand.value > 21:
            if len(player_hand.cards) > 2:
                player_bust(player_hand, dealer_hand, player_chips)
                break
            else:
                player_hand.check_ace
                pass

        #Player options
        hit_or_stand(deck, player_hand, player_chips)

        #Player busts if getting over 21 points when doubling down
        if player_hand.value > 21:
            show_all_cards(player_hand, dealer_hand)
            player_bust(player_hand, dealer_hand, player_chips)
            break

        #Show all cards on the board if player surrenders
        if surrender == False:
            show_some_cards(player_hand, dealer_hand)

    #BlackJack scenarios
    if player_hand.value == 21 and len(player_hand.cards) == 2:
        show_all_cards(player_hand, dealer_hand)
        print(green("\n*** BlackJack ***"))
        player_wins_bj(player_hand, dealer_hand, player_chips)
        
    elif dealer_hand.value == 21 and len(dealer_hand.cards) == 2:
        show_all_cards(player_hand, dealer_hand)
        print(red("\n*** BlackJack ***"))
        dealer_wins(player_hand, dealer_hand, player_chips)
        
    #Get 21 with more than two cards
    elif player_hand.value == 21:
        show_all_cards(player_hand, dealer_hand)
        player_wins(player_hand, dealer_hand, player_chips)
    
    elif dealer_hand.value == 21:
        show_all_cards(player_hand, dealer_hand)
        dealer_wins(player_hand, dealer_hand, player_chips)

    #Dealer wins if player surrenders
    elif surrender == True:
        show_all_cards(player_hand, dealer_hand)
        dealer_wins(player_hand, dealer_hand, player_chips)

    #Dealer playing
    elif player_hand.value < 21:
        #Dealer can't hit if the value of his hand is 17 or above
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)
        
        show_all_cards(player_hand, dealer_hand)

        #Other scenarios
        #Dealer bust
        if dealer_hand.value > 21:
            dealer_bust(player_hand, dealer_hand, player_chips)
        
        #Dealer win if his value is higher than the player's value
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        #Player win if value is higher than dealer's value
        elif player_hand.value > dealer_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        #When player and dealer value is equal
        else:
            push(player_hand, dealer_hand)

    time.sleep(1)
    #Player chips is increased if doubling down
    if double_down == True:
        player_chips.total *= 2
    
    #Player chips is halved if surrendering
    elif surrender == True:
        player_chips.total /= 2
    
    #Total amount of winning is increased
    winnings += player_chips.total

    print('\nWinnings: ', player_chips.total)
    time.sleep(1)
    #Game has ended and player is given some options
    #Player can't restart the game if theres no available chips
    restart = input("\nDo you want to:\n1. Continue playing\n2. Cash Out\n")
    if restart == '1':
        if winnings > 0:
            playing = True
            double_down = False
            surrender = False
            splitCount = 0
            continue
        elif winnings == 0:
            print("\nYou don't have enough chips, restart the game if you want to play again...")
            break
    else:
        print("\nYou got a total of %s chips" % winnings)
        print("\nThanks for playing")
        break
