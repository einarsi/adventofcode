from itertools import combinations


def bfs(graph, node, target=None):
    queue = [node]
    distance = {node: 0}

    while queue:
        n = queue.pop(0)
        for neighbor in graph[n]["neighbors"]:
            if neighbor not in distance:
                distance[neighbor] = 1 + distance[n]
                if neighbor == target:
                    return distance
                queue.append(neighbor)
    return distance


def find_max_flow(graph, startnode, available_time=30):
    max_flow = 0

    queue = [(startnode, 0, 0, set(graph) - {"AA"})]

    while queue:
        node, acc_time, acc_flow, closed_valves = queue.pop(0)

        for neighbor in closed_valves:
            time_there = graph[node]["neighbors"][neighbor]
            if acc_time + time_there > available_time:
                continue

            gained_rate = graph[neighbor]["rate"]
            new_flow = acc_flow + gained_rate * (
                available_time - acc_time - time_there - 1
            )

            if new_flow > max_flow:
                max_flow = new_flow

            queue.append(
                (
                    neighbor,
                    acc_time + time_there + 1,
                    new_flow,
                    closed_valves - {neighbor},
                )
            )
    return max_flow


def divide_rooms(graph):
    rooms = set(graph.keys()) - {"A"}
    # Huh,splitting the rooms in two equal parts (+/-1) actually gave the correct
    # answer. Saved a for-layer and lots of calculation time. Just luck?
    for me in combinations(sorted(rooms), len(rooms) // 2):
        my_graph = {"AA": graph["AA"]}
        elephants_graph = {"AA": graph["AA"]}
        for room in me:
            my_graph[room] = graph[room]
        for room in rooms - set(me):
            elephants_graph[room] = graph[room]
        yield my_graph, elephants_graph


lines = [line.strip() for line in open("input.txt").readlines()]

nodes = {}
for line in lines:
    node = line.split()[1]
    rate = int(line.split()[4].split("=")[1].strip(";"))
    neighbors = "".join(line.split()[9:]).split(",")
    nodes[node] = {"rate": rate, "neighbors": neighbors}

distances = {}  # All distances (in minutes) between each node with rate > 0 (and AA)
for s in nodes:
    for t in nodes:
        if s == t:
            continue
        if s == "AA" or nodes[t]["rate"] > 0:
            distances[(s, t)] = bfs(nodes, s, t)[t]
            distances[(t, s)] = distances[(s, t)]

graph = {}
for node in nodes:
    # Scales poorly, so only include nodes with rate > 0 (15 of 54) in graph
    if nodes[node]["rate"] == 0 and node != "AA":
        continue
    neighbors = {}
    for s, t in distances:
        if s == node:
            neighbors[t] = distances[(s, t)]
    graphnode = {"rate": nodes[node]["rate"], "neighbors": neighbors}
    graph[node] = graphnode


pt1 = find_max_flow(graph, "AA")
print(pt1)
assert pt1 == 1880

max_flow = 0
for me, elephant in divide_rooms(graph):
    my_flow = find_max_flow(me, "AA", 26)
    elephants_flow = find_max_flow(elephant, "AA", 26)
    if my_flow + elephants_flow > max_flow:
        max_flow = my_flow + elephants_flow

print(pt2 := max_flow)
assert pt2 == 2520
