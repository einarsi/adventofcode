from math import floor, sqrt

lines = [line.strip() for line in open("input.txt")]

times, distances = [
    list(map(int, line.strip().split(":")[1].split())) for line in lines
]

pt1 = 1
for time, distance in zip(times, distances):
    num_ways = 0
    for t in range(time):
        margin = t * (time - t) - distance
        num_ways += 1 if margin > 0 else 0
    pt1 *= num_ways

print(pt1)  # 512295

time, distance = [int(line.strip().split(":")[1].replace(" ", "")) for line in lines]

# Pt2 with finding start of interval where margin is positive (original solution)
start = 0
for t in range(time):
    margin = t * (time - t) - distance
    if margin > 0:
        start = t
        break

print(time - 2 * start + 1)  # 36530883

# Pt2 with brute force takes just 5 seconds
pt2 = 0
for t in range(time):
    margin = t * (time - t) - distance
    pt2 += 1 if margin > 0 else 0

print(pt2)  # 36530883

# Pt2 after realizing the interval start and stop can be found by solving a 2nd order inequality:
# (t * (time - t)) = d solved for t gives the beginning and end of the interval (+/- some decimals)
# t^2 - time * t + d = 0
# t = (time +/- sqrt(time^2 - 4*d))/2 = (time +/- s)/2 where s := sqrt(time^2-4*d)
# Due to symmetry: #possibilites = (t + s)/2-(t-s)/2 = s
# Turns out rounding down gives the correct answer.

print(floor(sqrt(time**2 - 4 * distance)))  # 36530883
