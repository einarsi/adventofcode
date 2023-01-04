import re

board, moves = open("input.txt").read().split("\n\n")

G = {}
for i, line in enumerate(board.split("\n")):
    for j, c in enumerate(line):
        if c == " ":
            continue
        G[i, j] = c

start = (0, min(k[1] for k in G if k[0] == 0 and G[k] == "."))

#      Right     Down    Left     Up
DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

#   012
# 0  UR
# 1  F
# 2 LD
# 3 B

faces = {
    "B": (3, 0),  # Back
    "L": (2, 0),  # Left
    "D": (2, 1),  # Down
    "F": (1, 1),  # Front
    "U": (0, 1),  # Up
    "R": (0, 2),  # Right
}


def get_face(pos, sz):
    for face, coords in faces.items():
        if coords[0] <= pos[0] // sz < coords[0] + 1 and coords[1] <= pos[1] // sz < coords[1] + 1:
            return face
    assert False, pos


assert get_face((160, 10), 50) == "B"
assert get_face((110, 10), 50) == "L"
assert get_face((10, 60), 50) == "U"
assert get_face((60, 60), 50) == "F"
assert get_face((110, 60), 50) == "D"
assert get_face((0, 110), 50) == "R"


def wrap(G, pos, d, cube=False):
    nxtd = d
    if not cube:
        if d == 0:  # right
            nxt = (pos[0], min(k[1] for k in G if k[0] == pos[0]))
        elif d == 2:  # left
            nxt = (pos[0], max(k[1] for k in G if k[0] == pos[0]))
        elif d == 1:  # down
            nxt = (min(k[0] for k in G if k[1] == pos[1]), pos[1])
        elif d == 3:  # up
            nxt = (max(k[0] for k in G if k[1] == pos[1]), pos[1])
        return nxt, nxtd
    else:
        # Solve cube for main input only since test input is different shape
        # We have crossed an edge and need to wrap to another side of the cube.
        # Find which edge we crossed from the departing face and direction we had.
        # Then translate and rotate position to new face and find corresponding new
        # direction on flat map.
        sz = 50
        face = get_face((pos[0] - DIRS[d][0], pos[1] - DIRS[d][1]), sz)
        if d == 0:  # right
            if face == "R":
                nxt = ((faces["D"][0] + 1) * sz - 1 - pos[0] % sz, faces["D"][1] * sz + sz - 1)
                nxtd = 2  # left
                assert get_face(nxt, sz) == "D"
            if face == "F":
                nxt = ((faces["R"][0] + 1) * sz - 1, faces["R"][1] * sz + pos[0] % sz)
                nxtd = 3  # up
                assert get_face(nxt, sz) == "R"
            if face == "D":
                nxt = ((faces["R"][0] + 1) * sz - 1 - pos[0] % sz, (faces["R"][1] + 1) * sz - 1)
                nxtd = 2  # left
                assert get_face(nxt, sz) == "R", nxt
            if face == "B":
                nxt = ((faces["D"][0] + 1) * sz - 1, faces["D"][1] * sz + pos[0] % sz)
                nxtd = 3  # up
                assert get_face(nxt, sz) == "D"
        elif d == 1:  # down
            if face == "B":
                nxt = (faces["R"][0] * sz, faces["R"][1] * sz + pos[1] % sz)
                nxtd = 1  # down
                assert get_face(nxt, sz) == "R"
            if face == "D":
                nxt = (faces["B"][0] * sz + pos[1] % sz, (faces["B"][1] + 1) * sz - 1)
                nxtd = 2  # left
                assert get_face(nxt, sz) == "B"
            if face == "R":
                nxt = (faces["F"][0] * sz + pos[1] % sz, (faces["F"][1] + 1) * sz - 1)
                nxtd = 2  # left
                assert get_face(nxt, sz) == "F"
        elif d == 2:  # left
            if face == "U":
                nxt = ((faces["L"][0] + 1) * sz - 1 - pos[0] % sz, faces["L"][1] * sz)
                nxtd = 0  # right
                assert get_face(nxt, sz) == "L", (pos, nxt)
            if face == "F":
                nxt = (faces["L"][0] * sz, faces["L"][1] * sz + pos[0] % sz)
                nxtd = 1  # down
                assert get_face(nxt, sz) == "L"
            if face == "L":
                nxt = ((faces["U"][0] + 1) * sz - 1 - pos[0] % sz, faces["U"][1] * sz)
                nxtd = 0  # right
                assert get_face(nxt, sz) == "U", (pos, nxt)
            if face == "B":
                nxt = (faces["U"][0] * sz, faces["U"][1] * sz + pos[0] % sz)
                nxtd = 1  # down
                assert get_face(nxt, sz) == "U"
        elif d == 3:  # up
            if face == "L":
                nxt = (faces["F"][0] * sz + pos[1] % sz, faces["F"][1] * sz)
                nxtd = 0  # right
                assert get_face(nxt, sz) == "F"
            if face == "U":
                nxt = (faces["B"][0] * sz + pos[0] % sz, faces["B"][1] * sz)
                nxtd = 0  # right
                assert get_face(nxt, sz) == "B"
            if face == "R":
                nxt = ((faces["B"][0] + 1) * sz - 1, faces["B"][1] * sz + pos[1] % sz)
                nxtd = 3  # up
                assert get_face(nxt, sz) == "B"
        return nxt, nxtd


def solve(G, instructions, pos, cube=False):
    d = 0
    for moves, rotation in re.findall(r"(\d+)([RL]?)", instructions):
        moves = int(moves)
        nxtd = d

        for _ in range(moves):
            nxt = (pos[0] + DIRS[d][0], pos[1] + DIRS[d][1])
            if nxt not in G:
                nxt, nxtd = wrap(G, nxt, d, cube=cube)

            if G[nxt] == "#":
                break
            pos = nxt
            d = nxtd

        d += {"R": 1, "L": -1}[rotation] if rotation in ["R", "L"] else 0
        d %= 4
    return pos, d


pos, d = solve(G, moves, start)
print(pt1 := 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + d)
assert pt1 == 131052

pos, d = solve(G, moves, start, cube=True)
print(pt2 := 1000 * (pos[0] + 1) + 4 * (pos[1] + 1) + d)
assert pt2 == 4578
