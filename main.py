from itertools import permutations
from sys import maxsize
import time


nr_of_vertexes = int(open("tsp_6_1.txt", "r").readline())


def costOfEdges(file):
    rows = open(file, "r").read().splitlines()
    cost_of_edges = []
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

    # print("Min cost: " + str(min_cost))
    # print("for path: " + str(cheapest_path))


def readFromIni(file):
    file = open(file, "r")
    rows = file.read().splitlines()
    data = []
    for r in range(1, len(rows)):
        data.append(rows[r].split())
    return data


def checkingFiles(data):
    nr_of_files = 8  # len(readFromIni(data))
    path = []
    for nr_of_file in range(nr_of_files):
        file_name = str(data[nr_of_file][0])
        repeat = int(data[nr_of_file][1])
        cost = int(data[nr_of_file][2])
        for v in range(3, len(data[nr_of_file])):
            path.append(data[nr_of_file][v])


# def printInfo(file, repeat, cost, path):
#     print("\n", file)
#     print(end - start)
#     print(cost)
#     print(path)


def saveToFile(file, repeat, cost, path):
    pass


def timingOneFile(file, repeat, cost, path):
    end = 0
    start = 0
    for r in range(repeat):
        start = time.time_ns()
        findCheapestPath(costOfEdges(file))
        end = time.time_ns()
        saveToFile(file, repeat, cost, path)


    print("\n", file)
    print(end - start)
    print(cost)
    print(path)


if __name__ == "__main__":
    # checkingFiles(readFromIni('porownanie.ini'))
    # findCheapestPath(costOfEdges("tsp_6_1.txt"))
    # print(readFromIni('porownanie.ini'))
    # file = "tsp_6_1.txt"
    # findCheapestPath(costOfEdges(file))
    path = [0, 11, 13, 2, 9, 10, 1, 12, 15, 14, 5, 6, 3, 4, 7, 8, 16, 0]
    timingOneFile("tsp_17.txt", 39, 132, path)

# print(data[0][0])
#     print(data[0][1])
#     print(data[0][2])
#     print(path)
