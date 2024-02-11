import sys

def prim(graph, vertices):
    # Initialize key values, parent array, and MST set
    key = [sys.maxsize] * vertices
    parent = [-1] * vertices
    mstSet = [False] * vertices

    # Starting vertex is chosen as 0
    key[0] = 0
    parent[0] = -1

    for _ in range(vertices):
        # Find the minimum key vertex from the set of vertices not yet included in MST
        u = minKey(key, mstSet, vertices)

        # Add the selected vertex to the MST set
        mstSet[u] = True

        # Update key values and parent index of adjacent vertices
        for v in range(vertices):
            if graph[u][v] and not mstSet[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    return parent, key

def minKey(key, mstSet, vertices):
    min_value = sys.maxsize
    min_index = -1

    for v in range(vertices):
        if key[v] < min_value and not mstSet[v]:
            min_value = key[v]
            min_index = v

    return min_index

def printMST(parent, graph, vertices):
    print("Edge \tWeight")
    for i in range(1, vertices):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")

def main():
    # Input the number of vertices
    vertices = int(input("Enter the number of vertices: "))

    # Input the adjacency matrix
    print("Enter the adjacency matrix (enter 0 for no edge):")
    graph = []
    for _ in range(vertices):
        row = list(map(int, input().split()))
        graph.append(row)

    # Run Prim's algorithm
    parent, key = prim(graph, vertices)

    # Print the minimum spanning tree
    print("\nMinimum Spanning Tree:")
    printMST(parent, graph, vertices)

    # Calculate and print the total weight of the minimum spanning tree
    total_weight = sum(key)
    print("\nTotal Weight of Minimum Spanning Tree:", total_weight)

if __name__ == "__main__":
    main()
