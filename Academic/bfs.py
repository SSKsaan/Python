def bfs(graph, start):
<<<<<<< HEAD
    visited = set()
    queue = [start]
    visited.add(start)
    
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
        
=======
    visited, queue = set([start]), [start]
    while queue:
        node = queue.pop(0)
        print(node, end=" ")
>>>>>>> a1ddb81c3be59fbc0cbdd27a50790fa3cdba8d56
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

<<<<<<< HEAD
def graph_input():
    graph = {}
    edges = int(input("Enter the number of edges: "))
    
    for _ in range(edges):
        u, v = input().split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)
    
=======
def graph_input(graph = {}):
    edges = int(input("Enter the number of edges in your graph: "))
    print("Enter the Edges (node1 node2): ")
    for _ in range(edges):
        u, v = input().split()
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
>>>>>>> a1ddb81c3be59fbc0cbdd27a50790fa3cdba8d56
    return graph

graph = graph_input()
start = input("Enter the starting node for BFS: ")
<<<<<<< HEAD

print("Breadth-First Search Traversal:")
=======
print("Breadth-First Search Traversal: ")
>>>>>>> a1ddb81c3be59fbc0cbdd27a50790fa3cdba8d56
bfs(graph, start)
print()