# Works, but very slow.

import math
from collections import deque

lines = [line.strip() for line in open("input.txt")]

B = []
DIRS = {">": (0, 1), "<": (0, -1), "^": (-1, 0), "v": (1, 0)}
for r, line in enumerate(lines[1:-1]):
    for c, ch in enumerate(line[1:-1]):
        if ch in DIRS.keys():
            B.append([(r, c), ch])

R = len(lines) - 2
C = len(lines[0]) - 2


def visualize(blizzards, mypos=None):
    if mypos is None:
        mypos = (-1, 0)
    for r in range(-1, R + 1):
        if r == -1:
            line = ["."] + ["#"] * (C - 1)
        elif r == R:
            line = ["#"] * (C - 1) + ["."]
        else:
            line = ["."] * C
            for b in blizzards:
                if b[0][0] == r:
                    if line[b[0][1]] == ".":
                        line[b[0][1]] = b[1]
                    elif line[b[0][1]] in DIRS.keys():
                        line[b[0][1]] = "2"
                    else:
                        line[b[0][1]] = str(int(line[b[0][1]]) + 1)
        if mypos[0] == r:
            line[mypos[1]] = "E"
        print("#" + "".join(line) + "#")


def move_blizzard(b, minutes):
    if b[1] in ["<", ">"]:
        return [(b[0][0], (b[0][1] + DIRS[b[1]][1] * minutes) % C), b[1]]
    return [((b[0][0] + DIRS[b[1]][0] * minutes) % R, b[0][1]), b[1]]


def available_slots(pos, blizzards, minutes):
    empty = set([(pos[0], pos[1])])
    for d in DIRS.values():
        empty.add((pos[0] + d[0], pos[1] + d[1]))
    for b0 in blizzards:
        if abs(b0[0][0] - pos[0]) <= 1 and b0[1] in ["<", ">"] or abs(b0[0][1] - pos[1]) <= 1 and b0[1] in ["^", "v"]:
            b = move_blizzard(b0, minutes)
            if b[0] in empty:
                empty.remove(b[0])
    return empty


def bfs(blizzards):
    start, goal = (-1, 0), (R, C - 1)
    lcm = R * C // math.gcd(R, C)

    queue = deque([(0, start)])
    seen = set()

    i = 0
    trip_num = 0
    while queue:
        i += 1
        if (i % 1000) == 0:
            print(i, len(seen))

        minutes, pos = queue.popleft()
        minutes += 1

        for slot in available_slots(pos, blizzards, minutes):
            if slot == goal and trip_num == 0:  # First crossing
                pt1 = minutes
                queue = deque([(minutes, slot)])
                seen = set()
                trip_num += 1
            elif slot == start and trip_num == 1:  # Back for snacks
                queue = deque([(minutes, slot)])
                seen = set()
                trip_num += 1
            elif slot == goal and trip_num == 2:  # Second crossing
                pt2 = minutes
                return (pt1, pt2)

            if not ((0 <= slot[0] < R and 0 <= slot[1] < C) or slot in [start, goal]):
                continue  # Outside map

            unique = (minutes % lcm, slot)
            if unique in seen:
                continue
            seen.add(unique)

            queue.append((minutes, slot))


pt1, pt2 = bfs(B)
print(pt1)
assert pt1 == 288
print(pt2)
assert pt2 == 861
