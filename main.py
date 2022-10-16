from sys import maxsize
vertexes = 4
edges = [[-1, 12, 13, 11], [12, -1, 14, 15], [13, 14, -1, 16], [11, 15, 16, -1]]
start_node = 0
path = [start_node]


def last_path(node, cost, start_node, min_cost, shortest_path):
    cost += edges[node][start_node]
    path.append(node)
    if cost < min_cost:
        return shortest_path[cost, path]
    return


def choose_path(node, cost, start_node, min_cost, shortest_path):
    for v in range(vertexes-1):
        if node != v:
            cost += edges[node][v]
            path.append(node)
            if len(path) == vertexes - 1:
                shortest_path = last_path(node, cost, start_node, min_cost, shortest_path)
                cost = 0
                path.clear()
                path.append(start_node)
                break
            else:
                choose_path(v, cost, start_node, min_cost, shortest_path)
    return shortest_path

if __name__ == "__main__":
    shortest_path = [0, 0]
    min_cost = 0
    cost = 0
    shortest_path = choose_path(start_node, cost, start_node, min_cost, shortest_path)
    # print('waga najkrotszej sciezki wynosi: ' + shortest_path[0])
    # print('kolejno odwiedzane wierzcholki: ' + shortest_path[1])