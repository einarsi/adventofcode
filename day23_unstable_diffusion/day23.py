lines = [line.strip() for line in open("input.txt")]

elves = {}
for i, line in enumerate(lines):
    line.strip()
    for j, c in enumerate(line):
        if c == "#":
            elves[i, j] = None

MOVEDIRS = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def scout_free_location(pos, d, occupied):
    for c in (-1, 0, 1):
        cd = (d[0] + c, d[1]) if d[0] == 0 else (d[0], d[1] + c)
        if (pos[0] + cd[0], pos[1] + cd[1]) in occupied:
            return False
    return True


def visualize(elves):
    minr = min(k[0] for k in elves)
    maxr = max(k[0] for k in elves)
    minc = min(k[1] for k in elves)
    maxc = max(k[1] for k in elves)

    for r in range(minr, maxr + 1):
        line = ""
        for c in range(minc, maxc + 1):
            line += "#" if (r, c) in elves else "."
        print(line)
    print()


elf_moved = True
i = 0
while elf_moved:
    elf_moved = False

    i += 1
    # if (i % 100) == 0:
    #     print(i)

    for elf in elves:
        if not all(scout_free_location(elf, d, elves) for d in MOVEDIRS):
            for d in MOVEDIRS:
                if scout_free_location(elf, d, elves):
                    elves[elf] = (elf[0] + d[0], elf[1] + d[1])
                    break

    all_newpos = list(elves.values())

    elves_after = {}
    for elf, newpos in elves.items():
        if newpos is None or all_newpos.count(newpos) > 1:
            elves_after[elf] = None
        else:
            elves_after[newpos] = None
            elf_moved = True

    elves = elves_after.copy()
    MOVEDIRS.append(MOVEDIRS.pop(0))

    if i == 10:
        minx = min(k[0] for k in elves)
        maxx = max(k[0] for k in elves)
        miny = min(k[1] for k in elves)
        maxy = max(k[1] for k in elves)
        print(pt1 := (maxx - minx + 1) * (maxy - miny + 1) - len(elves))
        assert pt1 == 3689

print(pt2 := i)
assert pt2 == 965
