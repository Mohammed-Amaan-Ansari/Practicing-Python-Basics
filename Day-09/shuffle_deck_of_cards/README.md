# Shuffle a Deck of Cards

## Problem

Create a deck of 52 playing cards and shuffle them randomly.

## Solution

import random

suits = ["♠", "♥", "♦", "♣"]
ranks = ["A", "2", ..., "K"]

deck = [f"{rank}{suit}" for suit in suits for rank in ranks]

random.shuffle(deck)

for card in deck:
    print(card)

## Sample Output
 
8♣
A♦
10♠
K♥
 

## Concepts Learned

- Lists
- List Comprehension
- random.shuffle()
- Nested Loops