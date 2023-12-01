lines = [line.strip() for line in open("input.txt")]

signal = [1]
for line in lines:
    signal.append(signal[-1])
    if line.startswith("addx"):
        num = int(line.split()[-1])
        signal.append(signal[-1] + num)

print(sum([i * signal[i - 1] for i in range(20, len(signal), 40)]))  # 13740

width = 40
screen = ""
for i in range(len(signal) - 1):
    sprite = signal[i]
    screen += "#" if sprite - 1 <= (i % width) <= sprite + 1 else "."

for i in range(0, len(screen), width):
    print(screen[i : i + width])  # ZUPRFECL
