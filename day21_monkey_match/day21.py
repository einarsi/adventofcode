def get_value(m):
    if isinstance(monkeys[m], int):
        return monkeys[m]
    else:
        monk1, op, monk2 = map(str.strip, monkeys[m].split())
        m1 = get_value(monk1)
        m2 = get_value(monk2)
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


def get_expression(m):
    if m == "humn":
        return "x"
    if isinstance(monkeys[m], int):
        return monkeys[m]

    monk1, op, monk2 = map(str.strip, monkeys[m].split())
    m1 = get_expression(monk1)
    m2 = get_expression(monk2)
    if (isinstance(m1, int)) and (isinstance(m2, int)):
        m1 = int(m1)
        m2 = int(m2)
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
    else:
        if op == "+":
            return f"({m1} + {m2})"
        elif op == "-":
            return f"({m1} - {m2})"
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

print("lhs:", lhsexpr)
print("rhs:", rhsexpr)

expr, const = (lhsexpr, rhsexpr) if "x" in lhsexpr else (rhsexpr, lhsexpr)

# Unfortunately expr is still somewhat convoluted, so can't easily solve for x.
# Do a crude search by halving an interval from max and min values for x.
# Sign check for diff depend on whether x enters expression with positive or
# negative sign. This happens happens to be opposite for the example and the input.

lolim = 0
hilim = int(1e15)
while lolim < hilim:
    x = (lolim + hilim) // 2
    diff = const - eval(expr)
    if diff < 0:
        lolim = x
    elif diff > 0:
        hilim = x
    else:
        lolim = hilim

print(pt2 := x)
assert pt2 == 3882224466191
