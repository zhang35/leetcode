from collections import deque


def dfs(graph, start):
    visited = set()  # keep track of the visited nodes
    stack = [start]  # use a stack to keep track of nodes to visit next

    while stack:
        node = stack.pop()  # get the next node to visit
        if node not in visited:
            visited.add(node)  # mark the node as visited
            print(node, end=' ')  # visit the node (print its value in this case)
            stack.extend(graph[node])  # add the node's neighbors to the stack
    print("")


def dfs_rec(graph, start):
    visited = set()

    def dfs(start): 
        print(start, end=" ")
        visited.add(start)
        for node in graph[start]:
            if node not in visited:
                dfs(node)

    dfs(start)
    print("")


def bfs(graph, start):
    visited = set()  # Keep track of the nodes that we've visited
    queue = deque([start])  # Use a queue to implement the BFS

    while queue:
        node = queue.popleft()  # Dequeue a node from front of queue
        if node not in visited:
            visited.add(node)  # Mark the node as visited
            print(node, end=' ')  # Visit the node (print its value in this case)
            queue.extend(graph[node])  # Enqueue all neighbours
    print("")


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E'],
}
dfs(graph, 'A')  # Output: A C F E B D
dfs_rec(graph, 'A')  # Output: A B D E F C
bfs(graph, 'A')  # Output: A B C D E F