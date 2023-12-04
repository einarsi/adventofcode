from collections import defaultdict

grid = [line.strip() for line in open("input.txt")]

dirs = [(-1, 0), (1, 0)]
dirs_left = [(0, -1), (-1, -1), (1, -1)]
dirs_right = [(0, 1), (-1, 1), (1, 1)]

pt1 = 0
gear_ratios = defaultdict(list)

numbers = {}
for m, row in enumerate(grid):
    number = ""
    for n, ch in enumerate(row + "."):
        if ch.isdigit():
            number += ch
        elif number:
            numbers[(m, n - len(number))] = number
            number = ""

for start_pos, number in numbers.items():
    done = False
    for i in range(len(number)):
        checkdirs = dirs.copy()
        if i == 0:
            checkdirs.extend(dirs_left)
        if i == len(number) - 1:
            checkdirs.extend(dirs_right)
        for d in checkdirs:
            m, n = start_pos[0] + d[0], start_pos[1] + i + d[1]
            if (
                0 <= m < len(grid)
                and 0 <= n < len(row)
                and grid[m][n] != "."
                and not grid[m][n].isdigit()
            ):
                pt1 += int(number)
                if grid[m][n] == "*":
                    gear_ratios[(m, n)].append(int(number))
                done = True
        if done:
            break

pt2 = sum(val[0] * val[1] for val in gear_ratios.values() if len(val) == 2)

print(pt1)  # 537732
print(pt2)  # 84883664
