# After having spent a somewhat significant amount time creating a
# routine to combine covered intervals to identify all covered points
# in a row in part 1, I decided to use the same routine to brute-force
# the solution to part 2. The solution appears after 3m 9 seconds, so
# not too bad.
# Having thought about it, I guess a (much) better solution would be
# to identify the four lines defining the boundaries for each sensor.
# Then look for a pair of lines with positive slope two units apart
# intersecting with another pair of parallell lines with negative slope
# like this:
# .\.../.
# \.\././
# .\.X./.
# ..X*X.. (* marks the spot)
# ./.X.\.
# /./.\.\
# But right now I can't be bothered... May revisit at some time


def dist(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def reduce_intervals(intervals):
    did_merge = True
    while did_merge:
        did_merge = False
        merged_intervals = []
        while len(intervals) > 0:
            e1 = intervals.pop()
            merged_e1 = False
            l = len(intervals)
            for i in range(l):
                e2 = intervals.pop(0)
                if not (min(e1) > max(e2) + 1 or min(e2) > max(e1) + 1):
                    merged_intervals.append(
                        (min(min(e1), min(e2)), max(max(e1), max(e2)))
                    )
                    did_merge = True
                    merged_e1 = True
                else:
                    intervals.append(e2)
                i += 1
            if not merged_e1:
                merged_intervals.append(e1)
        intervals = merged_intervals.copy()
    return intervals


assert reduce_intervals(
    [
        (-175434, 962182),
        (2628808, 3227288),
        (1649961, 2150357),
        (301283, 1516999),
        (3416034, 4415428),
        (1649961, 1737187),
        (2382651, 3109395),
        (-1095773, 1649961),
        (1649961, 3092243),
        (2985302, 4121574),
    ]
) == [(-1095773, 4415428)]

lines = [line.strip() for line in open("input.txt").readlines()]
row = 2000000
dimension = 4000000
# lines = [line.strip() for line in open("ex.txt").readlines()]
# row = 10
# dimension = 20

sensors = {}
for line in lines:
    ls = line.split()
    sx = int(ls[2].split("=")[1].split(",")[0])
    sy = int(ls[3].split("=")[1].split(":")[0])
    bx = int(ls[8].split("=")[1].split(",")[0])
    by = int(ls[9].split("=")[1].split(":")[0])
    sensors[(sx, sy)] = (bx, by)

intervals = []
for sensor, beacon in sensors.items():
    rng = dist(sensor, beacon) - abs(row - sensor[1])
    if rng >= 0:
        interval = (sensor[0] - rng, sensor[0] + rng)
        intervals.append(interval)

intervals = reduce_intervals(intervals)

beacons_in_row = 0
for interval in intervals:
    for beacon in set(sensors.values()):
        if beacon[1] == row and min(interval) <= beacon[0] <= max(interval):
            beacons_in_row += 1

a = sum(i[1] - i[0] + 1 for i in intervals)
print(pt1 := a - beacons_in_row)
assert pt1 == 5511201

for row in range(0, dimension + 1):
    if (row % 100000) == 0:
        print(row, end="")
    elif (row % 10000) == 0:
        print(".", end="")
    intervals = []
    for sensor, beacon in sensors.items():
        rng = dist(sensor, beacon) - abs(row - sensor[1])
        if rng >= 0:
            interval = (sensor[0] - rng, sensor[0] + rng)
            intervals.append(interval)
    intervals = reduce_intervals(intervals)
    if len(intervals) > 1:
        print()
        y = row
        x = sorted(intervals)[0][1] + 1
        print(pt2 := x * 4000000 + y)
        assert pt2 == 11318723411840
        assert False, "done"
