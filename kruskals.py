def kruskal_mst(vertices, edges):
    result = []
    edges = sorted(edges, key=lambda x: x[2])
    parent = [i for i in range(vertices)]
    rank = [0] * vertices

    def find_parent(i):
        if parent[i] == i:
            return i
        parent[i] = find_parent(parent[i])  # Path compression
        return parent[i]

    def union(u, v):
        u_root = find_parent(u)
        v_root = find_parent(v)
        if u_root != v_root:
            if rank[u_root] < rank[v_root]:
                parent[u_root] = v_root
            elif rank[u_root] > rank[v_root]:
                parent[v_root] = u_root
            else:
                parent[v_root] = u_root
                rank[u_root] += 1

    for u, v, w in edges:
        u_root = find_parent(u)
        v_root = find_parent(v)
        if u_root != v_root:
            result.append([u, v, w])
            union(u_root, v_root)

    print("Edges in the Minimum Spanning Tree:")
    for u, v, weight in result:
        print(u, "-", v, "\tWeight:", weight)


# Example usage:
vertices = 4
edges = [
    [0, 1, 10],
    [0, 2, 6],
    [0, 3, 5],
    [1, 3, 15],
    [2, 3, 4]
]

kruskal_mst(vertices, edges)
