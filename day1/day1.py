calories = []
elfs_calories = 0

for line in open("day1/input.txt", "r").readlines():
    if line != '\n':
        elfs_calories += int(line)
    else:
        calories.append(elfs_calories)
        elfs_calories = 0

calories.append(elfs_calories)

print(max(calories))
print(sum(sorted(calories)[-3:]))
