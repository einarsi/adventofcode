lines = [line.strip() for line in open("input.txt")]

pt1 = pt2 = 0

for line in lines:
    digits1 = []
    digits2 = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits1.append(c)
            digits2.append(c)
            continue
        for val, number in enumerate(
            ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        ):
            if line[i:].startswith(number):
                digits2.append(str(val + 1))
                break
    pt1 += int(digits1[0] + digits1[-1])
    pt2 += int(digits2[0] + digits2[-1])

print(pt1)  # 55029
print(pt2)  # 55686
