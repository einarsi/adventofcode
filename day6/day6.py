from collections import deque

data = open("day6/input.txt").read().strip()

# Deque makes the code more readable, less error prone to off-by-one
# errors and should be faster. Also more suited for an actual stream,
# since characters can be added as they arrive.

for ln in [4, 14]:
    d = deque(maxlen=ln)
    for i, c in enumerate(data):
        d.append(c)
        if len(set(d)) == ln:
            break
    print(i + 1)

# Original solution
# for ln in [4, 14]:
#     for i in range(ln, len(data) + 1):
#         if len(set(data[i - ln : i])) == ln:
#             break
#     print(i)
