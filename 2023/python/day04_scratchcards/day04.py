from collections import defaultdict

cards = [line.strip() for line in open("input.txt")]
mycards = defaultdict(lambda: 1)
pt1 = 0
pt2 = 0

for card in cards:
    id, data = card.split(":")
    id = int(id.split()[1])

    winning, mine = [set(map(int, group.split())) for group in data.split("|")]
    matches = len(winning & mine)

    pt1 += 2 ** (matches - 1) if matches > 0 else 0

    for i in range(matches):
        mycards[id + 1 + i] += mycards[id]
    pt2 += mycards[id]

print(pt1)  # 21959
print(pt2)  # 5132675
