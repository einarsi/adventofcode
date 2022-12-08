data = [line.strip() for line in open("day8/input.txt")]


def visible_trees(location, line):
    num = 0
    for tree in line:
        num += 1
        if tree >= location:
            break
    return max(num, 1)


forest = []
for row in data:
    forest.append([int(tree) for tree in row])

pt1 = 2 * (len(forest) + len(forest[0])) - 4
pt2 = 0
for i in range(1, len(forest) - 1):
    row = forest[i]
    for j in range(1, len(row) - 1):
        west = row[:j]
        east = row[j + 1 :]
        col = [row[j] for row in forest]
        north = col[:i]
        south = col[i + 1 :]

        pt1 += row[j] > min(
            [
                max(north, default=0),
                max(south, default=0),
                max(east, default=0),
                max(west, default=0),
            ]
        )
        tree = row[j]
        score = visible_trees(tree, reversed(west))
        score *= visible_trees(tree, east)
        score *= visible_trees(tree, reversed(north))
        score *= visible_trees(tree, south)

        pt2 = max(pt2, score)

print(pt1)
print(pt2)
