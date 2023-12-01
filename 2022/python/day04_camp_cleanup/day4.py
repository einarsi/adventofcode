contains = []
overlaps = []

for line in open("input.txt").readlines():
    pair = line.split(",")
    e1, e2 = [tuple(map(int, e)) for e in [elf.split("-") for elf in pair]]
    contains.append(
        (e1[0] >= e2[0] and e1[1] <= e2[1]) or (e1[0] <= e2[0] and e1[1] >= e2[1])
    )
    overlaps.append(
        (e1[0] <= e2[1] and e1[1] >= e2[0]) or (e1[1] >= e2[0] and e1[0] <= e2[1])
    )

print(contains.count(True))  # 503
print(overlaps.count(True))  # 827
