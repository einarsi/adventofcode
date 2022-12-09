def sign(x):
    return (1, -1)[x < 0]


lines = [line.strip() for line in open("input.txt")]

DIR = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

pos = [(0, 0) for _ in range(10)]  # head at 0
all_positions = [set([(0, 0)]) for _ in range(10)]

for line in lines:
    d, n = line.split()
    for _ in range(int(n)):
        move_x, move_y = DIR[d]
        pos[0] = (pos[0][0] + move_x, pos[0][1] + move_y)
        for k in range(1, len(pos)):
            dx, dy = (pos[k - 1][0] - pos[k][0], pos[k - 1][1] - pos[k][1])
            if max([abs(dx), abs(dy)]) <= 1:
                continue
            move_x = (abs(dx) > 1 or (abs(dy) > 1 and abs(dx) != 0)) * sign(dx)
            move_y = (abs(dy) > 1 or (abs(dx) > 1 and abs(dy) != 0)) * sign(dy)
            pos[k] = (pos[k][0] + move_x, pos[k][1] + move_y)
            all_positions[k].add(pos[k])

print(len(all_positions[1]))  # 6269
print(len(all_positions[9]))  # 2557
