def create_monkeys():
    monkeydefs = open("input.txt").read().split("\n\n")

    monkeys = []
    for monkeydef in monkeydefs:
        monkey = {"inspected": 0}
        for line in monkeydef.split("\n"):
            # This was a good candidate to get familiar with the structural
            # pattern matching introduced in Python 3.10
            match line.split():
                case ["Starting", "items:", *items]:
                    monkey["items"] = [int(item.strip(",")) for item in items]
                # eval is slooooow
                # case ["Operation:", "new", "=", *op]:
                #     monkey["operation"] = lambda old, op="".join(op): eval(op)
                case ["Operation:", *_, op, num]:
                    if op == "+":
                        monkey["operation"] = lambda old, num=int(num): old + num
                    else:
                        if num == "old":
                            monkey["operation"] = lambda old: old**2
                        else:
                            monkey["operation"] = lambda old, num=int(num): old * num
                case ["Test:", *_, divisor]:
                    monkey["divisor"] = int(divisor)
                case ["If", "true:", *_, throw_to]:
                    throw_true = int(throw_to)
                case ["If", "false:", *_, throw_to]:
                    throw_false = int(throw_to)
                case _:
                    pass
        monkey["throw_to"] = (throw_false, throw_true)

        monkeys.append(monkey)
    return monkeys


def reduce_monkey_business_pt1(n):
    return n // 3


def reduce_monkey_business_pt2(n):
    # If both x and y are divisible by p then n=(x+y) is also divisible by p.
    # Therefore: If we know that x is divisible by p, then we can check for divisibility
    # of n by p by only inspecting y. So let's keep n reasonably small by removing x
    # using n % x where x is the product of all divisors for monkey tests. Those go up
    # to 23 for the example, but 19 for the input. Hardcoded below.
    return n % (2 * 3 * 5 * 7 * 11 * 13 * 17 * 19 * 23)


def chase_monkeys(monkeys, rounds, reduce_monkey_business):
    for _ in range(rounds):
        for monkey in monkeys:
            for item in monkey["items"]:
                new = monkey["operation"](item)
                new = reduce_monkey_business(new)
                throw_to = monkey["throw_to"][new % monkey["divisor"] == 0]
                monkeys[throw_to]["items"].append(new)
                monkey["inspected"] += 1
            monkey["items"] = []
    return monkeys


for pt in [1, 2]:
    monkeys = create_monkeys()
    if pt == 1:
        ans = 58786
        monkeys = chase_monkeys(create_monkeys(), 20, reduce_monkey_business_pt1)
    else:
        ans = 14952185856
        monkeys = chase_monkeys(create_monkeys(), 10000, reduce_monkey_business_pt2)

    n_inspected = sorted([m["inspected"] for m in monkeys], reverse=True)
    print(pt := n_inspected[0] * n_inspected[1])
    assert pt == ans
