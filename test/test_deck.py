import unittest
from src.game_elements import Deck
from src.game_elements import Player
from src.game_elements import Card
from src.game_elements import calculate_total


class DeckTestCase(unittest.TestCase):

    def setUp(self):  # this method will be run before each test
        self.deck = Deck()

    def tearDown(self):  # this method will be run after each tests
        pass

    def test_number_of_cards(self):
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 52)
        
    def test_deal_one_reduces_size(self):
        self.deck.deal_one()
        number_of_cards = len(self.deck.cards)
        self.assertEqual(number_of_cards, 51)
        
class PlayerTestCase(unittest.TestCase):

    def setUp(self):
        self.player = Player('test')

    def tearDown(self):
        pass

    def test_add_card_increases_hand(self):
        card = Card('Hearts', 'Two')
        self.player.add_card(card)
        no_of_cards = len(self.player.hand)
        self.assertEqual(no_of_cards, 1)

class BlackjackTestCase(unittest.TestCase):
    def setUp(self):
        self.player = Player('test')

    def tearDown(self):
        pass
    
    # test calculate_total calculates aces correctlys
    def test_calculate_total(self):
        # create a hand with a single ace
        hand = [Card('Hearts', 'Ace'), Card('Spades', 'Three')]
        self.assertEqual(calculate_total(hand), 14)
        
        # create a hand with a single ace and a card worth 10
        hand = [Card('Hearts', 'Ace'), Card('Spades', 'King')]
        self.assertEqual(calculate_total(hand), 21)
        
        # create a hand with multiple aces
        hand = [Card('Hearts', 'Ace'), Card('Spades', 'Ace')]
        self.assertEqual(calculate_total(hand), 12)
        
        # create a hand with multiple aces and a total greater than 21
        hand = [Card('Hearts', 'Ace'), Card('Spades', 'Ace'), Card('Clubs', 'King')]
        self.assertEqual(calculate_total(hand), 12)

if __name__ == '__main__':
    unittest.main()
