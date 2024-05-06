import sys

def min_key(key, mst_set):
    min_val = sys.maxsize
    min_index = None
    for v in range(len(key)):
        if key[v] < min_val and mst_set[v] is False:
            min_val = key[v]
            min_index = v
    return min_index


def prim_mst(graph):
    V = len(graph)
    key = [sys.maxsize] * V
    parent = [None] * V
    key[0] = 0  # Starting node
    mst_set = [False] * V
    parent[0] = -1  # Root node has no parent
    total_cost = 0

    for _ in range(V):
        u = min_key(key, mst_set)
        mst_set[u] = True

        for v in range(V):
            if graph[u][v] > 0 and mst_set[v] is False and key[v] > graph[u][v]:
                key[v] = graph[u][v]
                parent[v] = u

    print("Edge \tWeight")
    for i in range(1, V):
        print(parent[i], "-", i, "\t", graph[i][parent[i]])
        total_cost += graph[i][parent[i]]

    print("Total cost of MST:", total_cost)


# Example usage:
graph = [
    [0, 2, 0, 6, 0],
    [2, 0, 3, 8, 5],
    [0, 3, 0, 0, 7],
    [6, 8, 0, 0, 9],
    [0, 5, 7, 9, 0]
]

prim_mst(graph)
