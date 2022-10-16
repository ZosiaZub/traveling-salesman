from sys import maxsize
from itertools import permutations

nr_of_vertexes = 4


def findShortestPath(graph, s_n):
    vertex = []
    for v in range(nr_of_vertexes):
        if v != s_n:
            vertex.append(v)

    min_path = maxsize
    next_permutation = permutations(vertex)

    for current_permutation in next_permutation:
        current_cost = 0

        start_vertex = s_n
        for end_vertex in current_permutation:
            current_cost += graph[start_vertex][end_vertex]
            start_vertex = end_vertex
        current_cost += graph[start_vertex][s_n]

        min_path = min(min_path, current_cost)

    return min_path



if __name__ == "__main__":

    edges = [[0, 10, 15, 20], [10, 0, 35, 25],
             [15, 35, 0, 30], [20, 25, 30, 0]]
    start_node = 0
    print(findShortestPath(edges, start_node))