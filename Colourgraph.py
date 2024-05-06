# Python3 program to implement greedy algorithm for graph coloring

def addEdge(adj, v, w):
    adj[v].append(w)
    adj[w].append(v)
    return adj

# Assigns colors (starting from 0) to all
# vertices and prints the assignment of colors
def greedyColoring(adj, V):
    result = [-1] * V

    # Assign the first color to first vertex
    result[0] = 0

    # A temporary array to store the available colors.
    # True value of available[cr] would mean that the
    # color cr is assigned to one of its adjacent vertices
    available = [False] * V

    # Assign colors to remaining V-1 vertices
    for u in range(1, V):
        # Process all adjacent vertices and
        # flag their colors as unavailable
        for i in adj[u]:
            if result[i] != -1:
                available[result[i]] = True

        # Find the first available color
        cr = 0
        while cr < V:
            if available[cr] == False:
                break
            cr += 1

        # Assign the found color
        result[u] = cr

        # Reset the values back to false
        # for the next iteration
        for i in adj[u]:
            if result[i] != -1:
                available[result[i]] = False

    # Print the result
    for u in range(V):
        print("Vertex", u, " ---> Color", result[u])

# Driver Code
if __name__ == '__main__':
    V = int(input("Enter the number of vertices: "))
    E = int(input("Enter the number of edges: "))

    adj = [[] for i in range(V)]
    print("Enter the edges (vertex1 vertex2): ")
    for i in range(E):
        v, w = map(int, input().split())
        adj = addEdge(adj, v, w)

    print("\nColoring of the graph: ")
    greedyColoring(adj, V)


# OP
# Enter the number of vertices: 5
# Enter the number of edges: 6
# Enter the edges (vertex1 vertex2):
# 0 1
# 1 2
# 0 3
# 3 4
# 4 0
# 2 3

# Coloring of the graph:
# Vertex 0  ---> Color 0
# Vertex 1  ---> Color 1
# Vertex 2  ---> Color 0
# Vertex 3  ---> Color 1
# Vertex 4  ---> Color 2
