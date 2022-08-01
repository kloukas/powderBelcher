import numpy as np

# Define the deck contents
deck = [
    'M','M','M','M','M','M','M','M',
    'R','R','R','R','R','R','R','R',
    'B','B','B','B','P','P','P','P',
    'T','T','T','T','T','T','T','T','T','T',
    'U','U','U','U','U','U','U','U','U','U','U','U','U',
    'F','F','F','F','F','F','F','F','F','F',
    'Z','Z','Z'
]

# Define all the acceptable/winning hands
winningHands = [
    ['B','T','U','U','R','R'],
    ['P','R','T','U','M'],
    ['B','U','U','U','R','R'],
    ['P','R','U','U','M'],
]

# How many times we want to run the simulation
count = 1000000

# Define a function to check for winning hand
def checkWin(hand, winningHands, deck):
    # Loop through all acceptable/winning hands
    for w in winningHands:

        # For each acceptable hand, go through the cards in the drawn hand and remove from the acceptable any that
        # appear in the drawn hand.
        copyWin = w.copy()
        for card in hand:
            if(card in copyWin):
                copyWin.remove(card)

        # If the list containing the winning card hand is empty this means all of the cards in the winning hand
        # appear in the drawn hand, exit and return true
        if not copyWin:
            return True

        # If we didn't win in the previous step check for a powder card
        elif 'Z' in hand:

            # If we find it we need to create a "Powder Deck" containing the original deck minus all cards drawn
            powderDeck = deck.copy()
            for x in hand:
                powderDeck.remove(x)

            # Draw a new hand from the "Powder Deck"
            newHand = np.random.choice(powderDeck, 7, False)
            # Check for win with the new hand 
            # This recursively calls the functions we are in, so pass the new "Powder Deck" in case we drew
            # another "Z" and need to generate a new Powder Deck again
            if checkWin(newHand, winningHands, powderDeck):
                return True

    # If we haven't won so far, the hand does not win so return false.
    return False



win = 0
for x in range(count):
    # Draw a random hand, check for win, if we won add 1 to the counter
    hand = np.random.choice(deck, 7, False)
    if checkWin(hand, winningHands, deck):
        win += 1

print(win/count)