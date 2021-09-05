import random
def koloda_cart():
    deck = ()
    for i in range(2, 11):
        for t in ('C', 'P', 'B', 'X'):
            deck.append(str(i) + t)
    for i in ('J', 'Q', 'K', 'T'):
        for t in ('C', 'P', 'B', 'X'):
            deck.append(i + t)
        return deck

def started_hand(deck):
    hand = []
    for i in range(2):
        hand.append(random.choice(deck))
        deck.remove(hand[-1])
    return hand, deck
    
def start_game():
    deck = create_deck()
    hand = []
    hand, deck = started_hand(deck)

start_game()


























            
