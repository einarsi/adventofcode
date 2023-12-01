def get_value(m):
    if isinstance(monkeys[m], float):
        return monkeys[m]
    else:
        monk1, op, monk2 = monkeys[m].split()
        m1 = get_value(monk1)
        m2 = get_value(monk2)
        if op == "+":
            return m1 + m2
        elif op == "-":
            return m1 - m2
        elif op == "*":
            return m1 * m2
        elif op == "/":
            return m1 / m2
        else:
            assert False


lines = [line.strip() for line in open("input.txt").readlines()]

monkeys = {}

for line in lines:
    m, o = line.split(":")
    o = o.strip()
    if o.isnumeric():
        monkeys[m.strip()] = float(o)
    else:
        monkeys[m.strip()] = o

monkeys_orig = monkeys.copy()

print(pt1 := int(get_value("root")))
assert pt1 == 21208142603224


def get_expression(m):
    if m == "humn":
        return "x"
    if isinstance(monkeys[m], float):
        return monkeys[m]

    monk1, op, monk2 = monkeys[m].split()
    m1 = get_expression(monk1)
    m2 = get_expression(monk2)
    if (isinstance(m1, float)) and (isinstance(m2, float)):
        m1 = float(m1)
        m2 = float(m2)
        if op == "+":
            return m1 + m2
        elif op == "-":
            return m1 - m2
        elif op == "*":
            return m1 * m2
        elif op == "/":
            return m1 / m2
        else:
            assert False
    else:
        return f"({m1} {op} {m2})"


monkeys = monkeys_orig.copy()

start = monkeys["root"].split("+")
lhstag = start[0].strip()
rhstag = start[1].strip()

lhsexpr = get_expression(lhstag)
rhsexpr = get_expression(rhstag)

print("lhs:", lhsexpr)
print("rhs:", rhsexpr)

expr, const = (lhsexpr, rhsexpr) if "x" in lhsexpr else (rhsexpr, lhsexpr)

# Do a binary search for x. Sign checks for diff depend on whether x enters
# expression with positive or negative sign. This happens happens to be opposite
# for the example and the input.

lolim = 0
hilim = int(1e13)
while lolim < hilim:
    x = (lolim + hilim) // 2
    diff = const - eval(expr)
    if diff < 0:
        lolim = x
    elif diff > 0:
        hilim = x
    else:
        lolim = hilim

print(pt2 := int(x))
assert pt2 == 3882224466191

# Analytical method using derivative since expr is linear in x. The delta for x
# to calculate the derivative must be very high to get correct result. Probably due
# to numerical precision effects.
# 0 = y(0) + y' * x
# x = y(0) / y'
x = 0
y0 = eval(expr) - const
x = 1e13
y1 = eval(expr) - const
dydx = (y1 - y0) / x
print(pt2 := int(-y0 / dydx))
assert pt2 == 3882224466191
