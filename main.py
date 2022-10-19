from itertools import permutations
from sys import maxsize


nr_of_vertexes = int(open("tsp_6_1.txt", "r").readline())


def costOfEdges(file):
    file = open(file, "r")
    cost_of_edges = []
    rows = file.read().splitlines()
    for r in range(1, nr_of_vertexes + 1):
        cost_of_edges.append(rows[r].split())
    return cost_of_edges


def allPaths(nr_of_v):
    vertexes = []
    for v in range(1, int(nr_of_v)):
        vertexes.append(v)
    return permutations(vertexes)


def findCheapestPath(cost_of_edges):
    min_cost = maxsize
    cheapest_path = []
    all_paths = allPaths(nr_of_vertexes)
    for path in all_paths:
        cost = 0
        start_vertex = 0
        for end_vertex in path:
            cost += int(cost_of_edges[start_vertex][end_vertex])
            start_vertex = end_vertex
        cost += int(cost_of_edges[start_vertex][0])

        if cost < min_cost:
            min_cost = cost
            cheapest_path.clear()
            cheapest_path.append(0)
            cheapest_path.extend(list(path))
            cheapest_path.append(0)

    print("Min cost: " + str(min_cost))
    print("for path: " + str(cheapest_path))


if __name__ == "__main__":
    findCheapestPath(costOfEdges("tsp_6_1.txt"))
