from src.game_elements import Deck
from src.game_elements import Card
from src.game_elements import Player
from src.game_elements import calculate_total

def play():
    while True:
        deck = Deck()
        deck.shuffle()
        
        player_one = Player("Player 1")
        dealer = Player("Dealer")
        
        # deal two cards to the player
        player_one.add_card(deck.deal_one())
        player_one.add_card(deck.deal_one())
        
        # deal two cards to the dealer
        dealer.add_card(deck.deal_one())
        dealer.add_card(deck.deal_one())
        
        # print the initial hands
        print(player_one.revealed_hand())
        print(dealer)
        
        # player's turn
        while True:
            print(f"Your current hand value is {calculate_total(player_one.hand)}.")
            choice = input("Would you like to hit or stand? (h/s)")
            if choice.lower() == 'h':
                # deal one card to the player
                new_card = deck.deal_one()
                player_one.add_card(new_card)
                print(f'You drew a {new_card}.')
                if calculate_total(player_one.hand) > 21:
                    print("You went bust!")
                    break
            elif choice.lower() == 's':
                break
            else:
                continue
        
        # dealer's turn
        while calculate_total(dealer.hand) < 17:
            new_card = deck.deal_one()
            dealer.add_card(new_card)
            print(f'Dealer drew a {new_card}!')
            if calculate_total(dealer.hand) > 21:
                print("Dealer went bust!")
                break
        
        p1_hand_val = calculate_total(player_one.hand)
        dealer_hand_val = calculate_total(dealer.hand)
        print('----------------------------')
        print(f"Player one's hand value is {p1_hand_val}")
        print(f'They had: {player_one.revealed_hand()}')
        print(f"Dealer's hand value is {dealer_hand_val}")
        print(f'They had: {dealer.revealed_hand()}')
        
        # compare hands
        if p1_hand_val > dealer_hand_val and p1_hand_val <= 21:
            print("You have won!")
            player_one.increment_wins()
        elif p1_hand_val <= 21 and dealer_hand_val > 21:
            print("You have won!")
            player_one.increment_wins()
        elif dealer_hand_val > p1_hand_val and dealer_hand_val <= 21:
            print("Dealer has won!")
        elif p1_hand_val > 21 and dealer_hand_val <= 21:
            print("Dealer has won!")
        elif p1_hand_val == dealer_hand_val:
            print("It's a tie!")
        else:
            print("Both players have lost!")
        
        print(f'Hands won: {player_one.hands_won}')
       
        play_again = input("Would you like to play again? (y/n)")
        if play_again == 'y':
            print('---------------------------- \n')
            continue
        else:
            break
# start the game
play()