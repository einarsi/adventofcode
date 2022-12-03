def item_to_val(item):
    val = ord(item)
    return val - 96 if val >= 97 else val - (64 - 26)


lines = [line.rstrip() for line in open("day3/input.txt", "r").readlines()]

in_both = []
for line in lines:
    middle = len(line) // 2
    common = set(line[:middle]) & set(line[middle:])
    in_both.append(common.pop())

stickers = []
for group in [lines[offset : offset + 3] for offset in range(0, len(lines), 3)]:
    stickers.append((set(group[0]) & set(group[1]) & set(group[2])).pop())

print(sum(item_to_val(b) for b in in_both))
print(sum(item_to_val(s) for s in stickers))
