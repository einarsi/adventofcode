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
        if G[pty - 1][ptx] != " ":
            return 0
    return -1


def hash_top_stack(i, j, topG):
    s = "".join([x for row in topG for x in row])
    return (i, j, hash(s))


def drop_rocks(numrocks):
    # Used complex numbers to represent rocks in the hope that pt2
    # would include rotation. No such luck...
    rock_shapes = [
        [0, 1, 2, 3],
        [1, 1j, 1 + 1j, 2 + 1j, 1 + 2j],
        [0, 1, 2, 2 + 1j, 2 + 2j],
        [0, 1j, 2j, 3j],
        [0, 1, 1j, 1 + 1j],
    ]

    G = [["+"] + ["-"] * 7 + ["+"]]

    seen_states = {}
    looped_height = 0
    looped_rocks = 0

    height = 0
    n = 0
    j = 0

    while n < numrocks - looped_rocks:
        shape = rock_shapes[n % len(rock_shapes)]

        x, y = 2 + 1, height + 4

        while len(G) < y + max([pt.imag for pt in shape]) + 1:
            G.append(["|"] + [" "] * 7 + ["|"])

        stopped = False
        k = 0
        while not stopped:
            wind = jets[j % len(jets)]
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
            j = (j + 1) % len(jets)

        height = max(height, y + max([int(pt.imag) for pt in shape]))

        fingerprint = hash_top_stack(
            n % len(rock_shapes), (j - 1) % len(jets), G[-20:-3]
        )
        if fingerprint in seen_states:
            stored_rocks, stored_height = seen_states[fingerprint]
            drocks = n - stored_rocks
            dheight = height - stored_height
            repeats = (numrocks - n) // drocks
            looped_height = repeats * dheight
            looped_rocks = repeats * drocks
            seen_states = {}
        else:
            seen_states[fingerprint] = (n, height)
        n += 1
    return height + looped_height


jets = open("input.txt").read().strip()

pt1 = drop_rocks(2022)
print(pt1)
assert pt1 == 3239

pt2 = drop_rocks(1_000_000_000_000)
print(pt2)
assert pt2 == 1594842406882
