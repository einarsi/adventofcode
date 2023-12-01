lines = [line.rstrip() for line in open("input.txt").readlines()]

s2d = {"0": 0, "1": 1, "2": 2, "-": -1, "=": -2}
d2s = {v: k for k, v in s2d.items()}

sum_base_10 = 0
for line in lines:
    for i, c in enumerate(reversed(line)):
        sum_base_10 += s2d[c] * (5**i)

sum_base_5 = []
while sum_base_10 > 0:
    sum_base_5.insert(0, sum_base_10 % 5)
    sum_base_10 //= 5

print(sum_base_5)
sum_snafu = sum_base_5.copy()

for i in range(len(sum_snafu)):
    sum_snafu[-i - 1] += (sum_snafu[-i] + 2) // 5
    sum_snafu[-i] = (sum_snafu[-i] + 2) % 5 - 2


print(pt1 := "".join(d2s[n] for n in sum_snafu))
assert pt1 == "2-2=21=0021=-02-1=-0"
