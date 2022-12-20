import random

suits = {'Hearts':'♥', 'Spades':'♠', 'Clubs':'♣', 'Diamonds':'♦'}
rank_values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':1}

# function to calculate the value of the cards in the player/dealer's hand
def calculate_total(hand):
    total = 0
    aces = 0
    for card in hand:
        if card.rank == 'Ace':
            aces += 1
        total += card.value

    # if we have an ace, and score has room to have ace value = 11 use it
    if  aces > 0 and total + 10 <= 21:
        total += 10
    return total

class Deck:
    def __init__(self):
        self.cards = []
        
        for suit in suits.keys():
            for rank in rank_values.keys():
                created_card = Card(suit, rank)
                self.cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.cards)
        
    def deal_one(self):
        return self.cards.pop()

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = rank_values[rank]
        
    def __str__(self):
        return f"{self.rank} of {suits[self.suit]}"
    
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.hands_won = 0
        
    def add_card(self, card):
        self.hand.append(card)
    
    def increment_wins(self):
        self.hands_won += 1
    
    def revealed_hand(self):
        card_str = ""
        for i in range(len(self.hand)-1):
            card_str += f'{self.hand[i]}, '
        card_str += f'and {self.hand[-1]}'
             
        return f"{self.name} has a {card_str}."
    
    def __str__(self):    
        return f"{self.name} has {len(self.hand)} cards."
       

