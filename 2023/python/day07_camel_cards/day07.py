from collections import Counter
from functools import partial

plays = [(hand, int(bid)) for hand, bid in (line.split() for line in open("input.txt"))]


# Replace jokers with (the same) value to find best hand
def replace_joker(hand):
    if "J" in hand:
        return max(handtype(hand.replace("J", card)) for card in "23456789TQKA")
    else:
        return handtype(hand)


# Map five-of-a-kind to 6, four-of-a-kind to 5, ..., one pair to 1, high-card to 0
def handtype(hand):
    counts = Counter(hand).values()
    if 5 in counts:
        return 6
    if 4 in counts:
        return 5
    if 3 in counts:
        return 4 if 2 in counts else 3
    if 2 in counts:
        return 2 if list(counts).count(2) == 2 else 1
    return 0


# Sorting order, numeric characters sort as lower than "a"
card_map = {"T": "a", "J": "b", "Q": "c", "K": "d", "A": "e"}


# Sort on two levels: type of hand first, then card values in sequence
def handstrength(play, pt2=False):
    hand = play[0]
    if pt2:
        card_map["J"] = "1"
    cardvalues = [card_map.get(card, card) for card in hand]
    if pt2:
        return (replace_joker(hand), cardvalues)
    return (handtype(hand), cardvalues)


pt1 = sum(
    rank * bid
    for rank, (_, bid) in enumerate(sorted(plays, key=partial(handstrength)), start=1)
)
print(pt1)  # 252656917

pt2 = sum(
    rank * bid
    for rank, (_, bid) in enumerate(
        sorted(plays, key=partial(handstrength, pt2=True)), start=1
    )
)
print(pt2)  # 253499763
