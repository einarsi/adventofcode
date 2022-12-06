data = open("day6/input.txt").read().strip()

for ln in [4, 14]:
    for i in range(ln, len(data) + 1):
        if len(set(data[i - ln : i])) == ln:
            break
    print(i)
