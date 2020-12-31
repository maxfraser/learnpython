from card import Card
import random

deck = []

ranks = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
suits = ["Clover", "Heart", "Diamond", "Spade"]

for suit in suits:
    for rank in ranks:
        card = Card(suit, rank)
        deck.append(card)

dealer_card_1 = random.choice(deck)
dealer_card_2 = random.choice(deck)

player_card_1 = random.choice(deck)
player_card_2 = random.choice(deck)

print(player_card_1)
print(player_card_2)
print("Dealer's hand is: " + str(dealer_card_1))

while True:
    player_input = input("Hit or Stand? ")

    if player_input == "stand":
        print(dealer_card_2)
    elif player_input == "quit":
        break
    else:
        player_card_3 = random.choice(deck)
        print(player_card_3)
