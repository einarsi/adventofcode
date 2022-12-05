setup, moves = open("day5/input.txt").read().split("\n\n")

setup = setup.split("\n")

numstacks = len(setup[-1].split())
stack1 = [[] for _ in range(numstacks)]
stack2 = [[] for _ in range(numstacks)]

for line in reversed(setup[:-1]):
    for i, j in enumerate(range(1, 1 + numstacks * 4, 4)):
        if line[j].isalpha():
            stack1[i].append(line[j])
            stack2[i].append(line[j])

for line in moves.split("\n"):
    _, num, _, source, _, dest = line.split()
    num, source, dest = map(int, [num, source, dest])
    for j in range(int(num)):
        stack1[dest - 1].append(stack1[source - 1].pop())

    stack2[dest - 1].extend(stack2[source - 1][-num:])
    del stack2[source - 1][-num:]

print("".join([stack[-1] for stack in stack1]))
print("".join([stack[-1] for stack in stack2]))
