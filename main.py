from itertools import permutations
from sys import maxsize
import time


def nrOfVertexes(file):
    return int(open(file, "r").readline())


def costOfEdges(file):
    rows = open(file, "r").read().splitlines()
    cost_of_edges = []
    for r in range(1, nrOfVertexes(file) + 1):
        cost_of_edges.append(rows[r].split())
    return cost_of_edges


def allPaths(nr_of_v):
    vertexes = []
    for v in range(1, int(nr_of_v)):
        vertexes.append(v)
    return permutations(vertexes)


def findCheapestPath(cost_of_edges, file):
    min_cost = maxsize
    cheapest_path = []
    all_paths = allPaths(nrOfVertexes(file))
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


def calculateDifference(file, repeat, csv_file):
    for r in range(repeat):
        start = time.time_ns()
        for r2 in range(10):
            findCheapestPath(costOfEdges(file), file)
        end = time.time_ns()
        difference = end - start
        csv_file.write(str(difference/10) + "\n")


def timingOneFile(file, repeat, csv_file):
    for r in range(int(repeat)):
        start = time.time_ns()
        findCheapestPath(costOfEdges(file), file)
        end = time.time_ns()
        difference = end - start
        csv_file.write(str(difference) + "\n")
    if file == "tsp_6_1.txt" or file == "tsp_6_2.txt":
        calculateDifference(file, repeat, csv_file)
    else:
        for r in range(int(repeat)):
            start = time.time_ns()
            findCheapestPath(costOfEdges(file), file)
            end = time.time_ns()
            difference = end - start
            csv_file.write(str(difference) + "\n")


def checkingFiles(file):

    csv_file = open("test_atsp_out.csv", "w")
    data = readFromIni(file)
    nr_of_files = len(data)
    for nr_of_file in range(nr_of_files):
        file_name = str(data[nr_of_file][0])
        repeat = int(data[nr_of_file][1])
        # cost = int(data[nr_of_file][2])
        # for v in range(3, len(data[nr_of_file])):
        #     path.append(data[nr_of_file][v])
        csv_file.write(str(data[nr_of_file]) + "\n")
        timingOneFile(file_name, repeat, csv_file)


if __name__ == "__main__":
    # checkingFiles(readFromIni('porownanie.ini'))
    # findCheapestPath(costOfEdges("tsp_6_1.txt"))
    # print(readFromIni('porownanie.ini'))
    # file = "tsp_6_1.txt"
    # findCheapestPath(costOfEdges(file))
    # path = [0, 10, 3, 5, 7, 9, 13, 11, 2, 6, 4, 8, 14, 1, 12, 0]
    # # [0, 11, 13, 2, 9, 10, 1, 12, 15, 14, 5, 6, 3, 4, 7, 8, 16, 0]
    # timingOneFile(readFromIni("tsp_6_1.txt"), 0)
    checkingFiles("porownanie.ini")

# print(data[0][0])
#     print(data[0][1])
#     print(data[0][2])
#     print(path)
