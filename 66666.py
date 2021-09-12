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
    deck = koloda_cart()
    hand = []
    hand, deck = started_hand(deck)
    while True:
        dopoln(hand, deck)
        
def give_card(deck):
    new_card = random.choice(deck)
    deck.remove(give_card)
    return new_card, deck
    
def dopoln(hand, deck):
    a = print('Будете добавлять?')
    if a.lower == 'да':
        d = give_card(deck)
        hand.append(d[0])
        deck = d[1]
    elif a.lower() == 'нет':
            exit()
    else:
        print('tot hfp')
    


















