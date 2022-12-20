## Blackjack
### by Finlay Earsman

I have created an object-orientated Python implementation of the card game "blackjack" for the BBC Software Engineering Graduate Scheme application process.

The way my implementation of the games works is as follows:

- There are two players, player 1 (the user) and the dealer (the computer).
- Both the dealer and the player are dealt two cards each from a deck of 52 cards.
- The player sees the value of their two cards and decides to "hit", get another card, or "stand" and pass the turn to the dealer.
- Dealer takes their turn, and once completed, the scores are evaluated to see who wins, loses or if there is a draw.
- If the player wins, their win counter is incremented.
- The player is then asked if they would like to play again. If so, the game resets. Otherwise, it exits the game.


### Assumption made
- The player cannot see any of the dealers cards before the game ends.
- There will only be two players, the player (user) and the dealer (computer).
- There are no benefits for getting something such as a "five card trick".
- The player cannot split their hand.