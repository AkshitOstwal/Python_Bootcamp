import random

suits = ('Hearts','Diamonds','Spades','Clubs')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two' : 2,'Three' : 3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}

playing = True

class Card:
    suit =[]
    rank =[]
    value  =[]
    def __init__(self,suit,rank,value):
        self.suit = suit
        self.rank = rank
        self.value = value
    def __str__(self):
        return "%s of %s and have value %s"%(self.rank,self.suit,self.value)

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                value = values[rank]
                self.deck.append(Card(suit,rank,value))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return 'the desk has \n'+deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces
    
    def add_card(self,card):
        #card passed in from Deck.deal()
        self.cards.append(card)
        self.value += card.value
        
        if card.rank == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        #if total value >21 and i still have an ace
        # than change my ace to be 1 instead of an 11
        
        while self.value>21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    
    def __init__(self,total=100):
        self.total = total  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

def take_bet(chips):
    while True:
        
        try:
            chips.bet = int(input('Enter amount you would like to bet'))
            break
        except:
            print('Enter only integer !!')
        else:
            if chips.bet > chips.total:
                print('you dont have enough chips you have : {}'.format(chips.total))
            else:
                break

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    while True:
        x = input('Hit or stand? Enter h or s')# hit #Hit #Stand
        if  x[0].lower() == 's':
            print('Player Stand dealer turn')
            playing = False
            break
        elif x[0].lower() == 'h':
            print('Player hit')
            hit(deck,hand)
            playing = True
            break
        else :
            print("wrong input,try again!!")
            continue 

def show_some(player,dealer):
    print("player hand")
    for card in player.cards:
        print(card)
    print('\ndealer hand one card hidden')
    for card in dealer.cards[1:]:
        print(card)
        
def show_all(player,dealer):
    print('player hand')
    for card in player.cards:
        print(card)
    print('Dealer hand')
    for card in dealer.cards:
        print(card)

def player_busts(player,dealer,chips):
    print('Bust player!!')
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("PLayer wins!!")
    chips.win_bet()
    
def dealer_busts(player,dealer,chips):
    print("player win!! Dealer busts!!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!!")
    chips.lose_bet()
    
def push(player,dealer):
    print('Dealer and player tie! push')

while True:
    # Print an opening statement
    print("hello and welcome to the BlackJack game")
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    player.add_card(deck.deal())
    dealer.add_card(deck.deal())
    
        
    # Set up the Player's chips
    chips = Chips(100)
    
    # Prompt the Player for their bet
    print('Now its time to make your first bet')
    take_bet(chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player,dealer)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        print('NOw its time to make a Hit or Stand')
        hit_or_stand(deck,player)
        
        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player.value > 21:
            player_busts(player,dealer,chips)
            show_all(player,dealer)

            break

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
    if player.value <= 21:
            
        while dealer.value < 17:
            hit(deck,dealer)

        # Show all cards
        show_all(player,dealer)

        # Run different winning scenarios
        if dealer.value >21 :
            dealer_busts(player,dealer,chips)
        elif dealer.value > player.value:
            dealer_wins(player,dealer,chips)
        elif dealer.value < player.value:
            player_wins(player,dealer,chips)
        else:
            push(player,dealer)


    # Inform Player of their chips total 
    print("\n Player total chips are :{} ".format(chips.total))
        
    # Ask to play again
    if input("Wanna play again 'y' or 'n' ").lower() == 'y':
        playing = True
        continue
    else:
        break
