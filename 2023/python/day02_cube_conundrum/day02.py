lines = [line.strip() for line in open("input.txt")]

maxcubes = {"red": 12, "green": 13, "blue": 14}

pt1 = pt2 = 0

for line in lines:
    possible = True
    mincubes = {"red": 0, "green": 0, "blue": 0}

    gameid, pulls = line.split(":")
    for pull in pulls.split(";"):
        for numcolor in pull.split(","):
            num, color = numcolor.strip().split(" ")
            if int(num) > maxcubes[color]:
                possible = False
            mincubes[color] = max(mincubes[color], int(num))
    if possible:
        pt1 += int(gameid.split(" ")[1])
    pt2 += mincubes["red"] * mincubes["green"] * mincubes["blue"]

print(pt1)  # 2076
print(pt2)  # 70950
