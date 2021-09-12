import random
def koloda_cart():
    deck = []
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
        print_hand(hand)
        print_score(hand)
        dopoln(hand, deck)
        
def give_card(deck):
    new_card = random.choice(deck)
    deck.remove(new_card)
    return new_card, deck
    
def dopoln(hand, deck):
    a = input('Будете добавлять?')
    if a.lower() == 'да':
        d = give_card(deck)
        hand.append(d[0])
        deck = d[1]
    elif a.lower() == 'нет':
            exit()
    else:
        print('еще раз')

def print_hand(hand):
    for card in hand:
        print(card, end = ' ')
    print()

def print_score(hand):
    costs = {
        "2": 2,  
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "1": 10,
        "J": 2,
        "Q": 3,
        "K": 4,
        "T": 11
    }
    score = 0
    for card in hand:
        score += costs[card[0]]

    print(score)



    
start_game()







