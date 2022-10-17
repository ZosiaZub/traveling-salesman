import fileinput
from itertools import permutations

#nr_of_vertexes = fileinput.input("moje_dane.txt")


def costOfEdges(file_name):
    file = open(file_name, "r")
    lines = file.read().splitlines()
    cost_of_edges = []
    for i in range(1, len(lines)):
        cost_of_edges.append(lines[i].split())
    return cost_of_edges


def nrOfVertexes(file_name):
    file = open(file_name, "r")
    return file.readline()


def allRouts(start_node, nr_of_vertexes):
    vertexes = []
    for node in range(int(nr_of_vertexes)):
        if node != start_node:
            vertexes.append(node)
    return permutations(vertexes)


def findShortestRout(data, number_of_cities):
    min_rout = 2147483647
    all_routs = allRouts(0, number_of_cities)
    for route in all_routs:
        cost = 0
        i = 0
        for vertex in route:
            cost += int(data[i][vertex])
            i = vertex

        cost += int(data[i][0])
        if cost < min_rout:
            min_rout = cost
    print(min_rout)


if __name__ == "__main__":
    findShortestRout(costOfEdges("moje_dane.txt"), nrOfVertexes("moje_dane.txt"))
