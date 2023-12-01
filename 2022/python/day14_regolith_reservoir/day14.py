def make_grid(M, N, empty_char=" ", has_floor=False):
    grid = []
    for i in range(M + 1):
        r = [empty_char for _ in range(N)]
        grid.append(r)

    for path in paths:
        for i in range(len(path) - 1):
            seg1x, seg1y = path[i]
            seg2x, seg2y = path[i + 1]
            for m in range(min(seg1y, seg2y), max(seg1y, seg2y) + 1):
                for n in range(min(seg1x, seg2x), max(seg1x, seg2x) + 1):
                    grid[m][n - minx] = "#"
    if has_floor:
        grid.append([empty_char for _ in range(N)])
        grid.append(["#" for _ in range(N)])

    return grid


def drop_sand(grid, insert_pt, empty_char=" ", has_floor=False):
    grid[0][insert_pt] = "+"
    i = 0

    while True:
        m = 0
        n = insert_pt
        while has_floor or m < len(grid) - 1:
            if n == 0:  # expand grid left
                for row in grid:
                    row.insert(0, empty_char)
                grid[-1][0] = "#" if has_floor else grid[-1][0]
                insert_pt += 1
                n += 1
            elif n == len(grid[0]) - 1:  # expand grid right
                for row in grid:
                    row.append(empty_char)
                grid[-1][-1] = "#" if has_floor else grid[-1][-1]
            if grid[m + 1][n] == empty_char:
                m += 1
            elif grid[m + 1][n - 1] == empty_char:
                m += 1
                n -= 1
            elif grid[m + 1][n + 1] == empty_char:
                m += 1
                n += 1
            else:
                break
        else:
            break  # sand falls out of bounds
        i += 1
        grid[m][n] = "o"
        if m == 0:  # sand insert pt clogged
            break
    return i


lines = [line.strip() for line in open("input.txt").readlines()]

minx = float("inf")
maxx = maxy = 0
paths = []
for line in lines:
    path = []
    for segment in line.split("->"):
        x, y = map(int, segment.split(","))
        path.append((x, y))
        minx = min(minx, x)
        maxx = max(maxx, x)
        maxy = max(maxy, y)
    paths.append(path)

M = maxy
N = maxx - minx + 1
empty = "."
grid = make_grid(M, N, empty_char=empty)

pt1 = drop_sand(grid, 500 - minx, empty_char=empty)
print(pt1)
assert pt1 == 757

grid = make_grid(M, N, empty_char=empty, has_floor=True)

pt2 = drop_sand(grid, 500 - minx, empty_char=empty, has_floor=True)
print(pt2)
assert pt2 == 24943
# for row in grid:
#     print("".join(row))
