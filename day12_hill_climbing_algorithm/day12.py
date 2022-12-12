import heapq
import sys
from collections import defaultdict

lines = [line.strip() for line in open("input.txt")]

grid = {}

for y, line in enumerate(lines):
    for x, c in enumerate(line.strip()):
        if c.islower():
            grid[(x, y)] = ord(c) - ord("a")
        else:
            if c == "S":
                startnode = (x, y)
                grid[(x, y)] = 0
            elif c == "E":
                endnode = (x, y)
                grid[(x, y)] = ord("z") - ord("a")

assert isinstance(startnode, tuple)
assert isinstance(endnode, tuple)

Y = len(lines)
X = len(lines[0])


def get_neighbors(grid, node):
    neighbors = []
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        neighbor = (node[0] + dx, node[1] + dy)
        if (
            0 <= neighbor[0] < X
            and 0 <= neighbor[1] < Y
            and grid[neighbor] <= grid[node] + 1
        ):
            neighbors.append(neighbor)
    return neighbors


def dijkstra(grid, startnode, endnode):
    queue = []
    heapq.heappush(queue, (0, startnode))
    costs = defaultdict(lambda: int(sys.maxsize))
    costs[startnode] = 0
    seen = set()

    while queue:
        _, node = heapq.heappop(queue)
        if node == endnode:
            return costs
        seen.add(node)

        for neighbor in get_neighbors(grid, node):
            if neighbor in seen:
                continue

            if (new_cost := costs[node] + 1) < costs[neighbor]:
                costs[neighbor] = new_cost
                heapq.heappush(queue, (new_cost, neighbor))
    return costs


costs = dijkstra(grid, startnode, endnode)

print(pt1 := costs[endnode])
assert pt1 == 468

shortest = sys.maxsize
for node in grid.keys():
    if grid[node] == 0:
        costs = dijkstra(grid, node, endnode)
        shortest = min(costs[endnode], shortest)

print(pt2 := shortest)
assert pt2 == 459
