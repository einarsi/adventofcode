from collections import deque

lines = [line.strip() for line in open("input.txt").readlines()]

cubes = {tuple(map(int, line.split(","))) for line in lines}

droplet = set()
exposed = 0

for cube in cubes:
    exposed += 6
    for segment in droplet:
        for i in range(3):
            if (
                abs(segment[i] - cube[i]) == 1
                and segment[(i + 1) % 3] == cube[(i + 1) % 3]
                and segment[(i + 2) % 3] == cube[(i + 2) % 3]
            ):
                exposed -= 2
    droplet.add(cube)

print(pt1 := exposed)
assert pt1 == 4340

# Calculate bounding box 1 larger than droplet
minxyz = [float("inf")] * 3
maxxyz = [float("-inf")] * 3
for cube in cubes:
    minxyz = [min(x, y) for x, y in zip(minxyz, cube)]
    maxxyz = [max(x, y) for x, y in zip(maxxyz, cube)]
minxyz = [t - 1 for t in minxyz]
maxxyz = [t + 1 for t in maxxyz]

# Which points can be reached from outside? Start at one corner of BB
queue = deque([tuple(minxyz)])
outside = {tuple(minxyz)}
while queue:
    p = queue.popleft()
    for d in ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1)):
        np = tuple(x + y for x, y in zip(p, d))
        if not (minxyz[0] <= np[0] <= maxxyz[0]):
            continue
        if not (minxyz[1] <= np[1] <= maxxyz[1]):
            continue
        if not (minxyz[2] <= np[2] <= maxxyz[2]):
            continue
        if np in droplet or np in outside:
            continue
        queue.append(np)
        outside.add(np)

# Identify pockets as all voxels that are not air nor droplet within BB
pockets = []
for x in range(minxyz[0] + 1, maxxyz[0]):
    for y in range(minxyz[1] + 1, maxxyz[1]):
        for z in range(minxyz[2] + 1, maxxyz[2]):
            if (p := tuple([x, y, z])) in (droplet | outside):
                continue
            pockets.append(p)

# Count all surfaces between droplet and airpockets
airpocket_surfaces = 0
for p in pockets:
    for d in droplet:
        for i in range(3):
            if (
                abs(d[i] - p[i]) == 1
                and d[(i + 1) % 3] == p[(i + 1) % 3]
                and d[(i + 2) % 3] == p[(i + 2) % 3]
            ):
                airpocket_surfaces += 1

print(pt2 := exposed - airpocket_surfaces)
assert pt2 == 2468
