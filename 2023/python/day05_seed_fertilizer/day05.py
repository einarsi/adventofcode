sections = open("input.txt").read().split("\n\n")

seeds = list(map(int, sections[0].split(":")[1].split()))

maps = []
for section in sections[1:]:
    thismap = []
    for line in section.split("\n")[1:]:
        thismap.append(list(map(int, line.split())))
    maps.append(thismap)

inputs = seeds
for m in maps:
    outputs = []
    for input in inputs:
        for dest, src, length in m:
            if src <= input < src + length:
                outputs.append(dest + (input - src))
                break
        else:
            outputs.append(input)
    inputs = outputs

print(min(outputs))  # 289863851

inputs = [(start, start + length) for start, length in zip(seeds[::2], seeds[1::2])]
for m in maps:
    outputs = []
    while len(inputs) > 0:
        begin, end = inputs.pop()
        for dest, src, length in m:
            interval_begin = max(begin, src)
            interval_end = min(end, src + length)
            if interval_begin < interval_end:
                outputs.append(
                    (dest + (interval_begin - src), dest + (interval_end - src))
                )
                if begin < interval_begin:
                    inputs.append((begin, interval_begin))
                if end > interval_end:
                    inputs.append((interval_end, end))
                break
        else:
            outputs.append((begin, end))
    inputs = outputs

print(min(min(outputs)))  # 60568880
