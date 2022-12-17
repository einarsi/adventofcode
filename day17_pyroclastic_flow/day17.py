motion = open("input.txt").read().strip()

# Used complex numbers to represent rocks in the hope that pt2
# would include rotation. No such luck...

rocks = [
    [0, 1, 2, 3],
    [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],
    [0, 1, 2, 2 + 1j, 2 + 2j],
    [0, 1j, 2j, 3j],
    [0, 1, 1j, 1 + 1j],
]

width = 7


def blow(G, shape, x, y, wind):
    dx = -1 if wind == "<" else 1

    for pt in shape:
        ptx = x + int(pt.real)
        pty = y + int(pt.imag)
        if G[pty][ptx + dx] != " ":
            return 0
    return dx


def drop(G, shape, x, y):
    for pt in shape:
        ptx = x + int(pt.real)
        pty = y + int(pt.imag)
        if pty - 1 < 1:
            return 0
        elif G[pty - 1][ptx] != " ":
            return 0
    return -1


G = [["+"] + ["-"] * 7 + ["+"]]
height = 0
j = 0

for i in range(2022):
    shape = rocks[i % len(rocks)]

    x, y = 2 + 1, height + 4

    while len(G) < y + max([pt.imag for pt in shape]) + 1:
        G.append(["|"] + [" "] * 7 + ["|"])

    stopped = False
    k = 0
    while not stopped:
        wind = motion[j % len(motion)]
        x += blow(G, shape, x, y, wind)
        if k < 3:  # Don't check for contact while freefalling
            y -= 1
        else:
            dy = drop(G, shape, x, y)
            if dy:
                y += dy
            else:
                for pt in shape:
                    G[y + int(pt.imag)][x + int(pt.real)] = "#"
                    stopped = True
        k += 1
        j += 1
    height = max(height, y + max([int(pt.imag) for pt in shape]))


pt1 = height
assert pt1 == 3239

# pt2:
# for i in range(1_000_000_000_000) ...!
# Small optimizations that won't really help with scaling:
# - Check only right- and leftmost point(s) in shape when blowing
# - Check only bottom point(s) in shape when dropping
# Memory-saving:
# - Discard lower parts of G if no rocks can get there, Kinda tricky to do?
#   Perhaps only retain the part of G higher than the highest point where it
#   is closed-off. "closed-off" needs to be determined
# There must be a smarter way to solve this quickly
