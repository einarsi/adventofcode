def get_value(m):
    if isinstance(monkeys[m], int):
        return monkeys[m]
    else:
        monk1, op, monk2 = monkeys[m].split()
        monk1 = monk1.strip()
        monk2 = monk2.strip()
        m1 = get_value(monk1)
        m2 = get_value(monk2)
        op = op.strip()
        if op == "+":
            return m1 + m2
        elif op == "-":
            return m1 - m2
        elif op == "*":
            return m1 * m2
        elif op == "/":
            return m1 // m2
        else:
            assert False


lines = [line.strip() for line in open("input.txt").readlines()]

monkeys = {}

for line in lines:
    m, o = line.split(":")
    o = o.strip()
    if o.isnumeric():
        monkeys[m.strip()] = int(o)
    else:
        monkeys[m.strip()] = o

monkeys_orig = monkeys.copy()

print(pt1 := get_value("root"))
assert pt1 == 21208142603224

# pt2 is WIP


def get_expression(m):
    if m == "humn":
        return "x"
    if isinstance(monkeys[m], int):
        return monkeys[m]

    if not (
        "+" in monkeys[m] or "-" in monkeys[m] or "*" in monkeys[m] or "/" in monkeys[m]
    ):
        return monkeys[m]
    monk1, op, monk2 = monkeys[m].split()
    monk1 = monk1.strip()
    monk2 = monk2.strip()
    m1 = get_expression(monk1)
    m2 = get_expression(monk2)
    op = op.strip()
    if op == "+":
        return f"({m1} + {m2})"
    elif op == "-":
        return f"({m1}) - ({m2})"
    elif op == "*":
        return f"{m1} * {m2}"
    elif op == "/":
        return f"{m1} // {m2}"
    else:
        assert False


monkeys = monkeys_orig.copy()

start = monkeys["root"].split("+")
lhstag = start[0].strip()
rhstag = start[1].strip()

lhsexpr = get_expression(lhstag)
rhsexpr = get_expression(rhstag)

# print(lhsexpr)
# print(rhsexpr)

print(eval(rhsexpr))

if "x" in lhsexpr:
    rhs = eval(rhsexpr)

    for x in range(1000):
        if rhs == eval(lhsexpr):
            print(x)
        break
# elif "x" in rhsexpr:
#     lhs = eval(lhsexpr)

#     for x in range(1000):
#         rhs = eval(rhsexpr)
#         print(rhs)
