from collections import deque

lines = [line.strip() for line in open("input.txt").readlines()]

droplet = {tuple(map(int, line.split(","))) for line in lines}

pt1 = 0
for v in droplet:
    for d in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
        np = tuple(x + y for x, y in zip(v, d))
        if np not in droplet:
            pt1 += 1

print(pt1)
assert pt1 == 4340

# Calculate bounding box 1 larger than droplet
minxyz = [float("inf")] * 3
maxxyz = [float("-inf")] * 3
for v in droplet:
    minxyz = [min(x, y) for x, y in zip(minxyz, v)]
    maxxyz = [max(x, y) for x, y in zip(maxxyz, v)]
minxyz = [t - 1 for t in minxyz]
maxxyz = [t + 1 for t in maxxyz]


queue = deque([minxyz])
seen = {tuple(minxyz)}

pt2 = 0
while queue:
    v = queue.popleft()
    for d in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)]:
        np = tuple(x + y for x, y in zip(v, d))
        if np in seen:
            continue
        if not (minxyz[0] <= np[0] <= maxxyz[0]):
            continue
        if not (minxyz[1] <= np[1] <= maxxyz[1]):
            continue
        if not (minxyz[2] <= np[2] <= maxxyz[2]):
            continue
        if np in droplet:
            pt2 += 1
        else:
            queue.append(np)
            seen.add(np)
print(pt2)
assert pt2 == 2468
