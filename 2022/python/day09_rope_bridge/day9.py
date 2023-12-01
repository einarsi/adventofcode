lines = [line.strip() for line in open("input.txt")]

DIR = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

knots = [(0, 0) for _ in range(10)]  # head at 0
positions = [set([(0, 0)]) for _ in range(10)]

for line in lines:
    d, n = line.split()
    for _ in range(int(n)):
        move_x, move_y = DIR[d]
        knots[0] = (knots[0][0] + move_x, knots[0][1] + move_y)
        for k in range(1, len(knots)):
            dx, dy = (knots[k - 1][0] - knots[k][0], knots[k - 1][1] - knots[k][1])
            if max([abs(dx), abs(dy)]) <= 1:
                continue
            move_x = (dx > 0) - (dx < 0)
            move_y = (dy > 0) - (dy < 0)
            knots[k] = (knots[k][0] + move_x, knots[k][1] + move_y)
            positions[k].add(knots[k])

print(len(positions[1]))  # 6269
print(len(positions[9]))  # 2557
