from functools import cmp_to_key


def compare(l, r):
    if isinstance(l, int) and isinstance(r, int):
        return (l > r) - (l < r)
    l = list((l,)) if isinstance(l, int) else l
    r = list((r,)) if isinstance(r, int) else r
    for ll, rr in zip(l, r):
        cmp = compare(ll, rr)
        if cmp != 0:
            return cmp
    return (len(l) > len(r)) - (len(l) < len(r))


pairlines = [p for p in open("input.txt").read().split("\n\n")]

pckt_pairs = []
for p in pairlines:
    l, r = map(eval, p.split())
    pckt_pairs.append((l, r))

pt1 = 0
for i, pair in enumerate(pckt_pairs, start=1):
    if compare(pair[0], pair[1]) == -1:
        pt1 += i

print(pt1)
assert pt1 == 5825

dividers = ([[2]], [[6]])
pckts = [p for pair in pckt_pairs for p in pair]
pckts.extend(dividers)

pckts.sort(key=cmp_to_key(compare))
print(pt2 := (pckts.index(dividers[0]) + 1) * (pckts.index(dividers[1]) + 1))
assert pt2 == 24477
