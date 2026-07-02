import random

suits = ["♠", "♥", "♦", "♣"]
ranks = ["A", "2", "3", "4", "5", "6", "7", "8",
         "9", "10", "J", "Q", "K"]

deck = [f"{rank}{suit}" for suit in suits for rank in ranks]

random.shuffle(deck)

print("Shuffled Deck:")

for card in deck:
    print(card)