from collections import deque

labels = ['P', 'I', 'O', 'D', 'O', 'S']
adj = {i: [] for i in range(len(labels))}


def add_edge(u, v):
    adj[u].append(v)
    adj[v].append(u)  # Undirected graph edge


def bfs(start):
    visited = [False] * len(labels)
    queue = deque([start])
    visited[start] = True
    result = []

    while queue:
        curr = queue.popleft()
        result.append(labels[curr])

        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    print("Graph BFS:", " - ".join(result))


def dfs(curr, visited=None, result=None):
    if visited is None:
        visited = [False] * len(labels)
    if result is None:
        result = []

    visited[curr] = True
    result.append(labels[curr])

    for neighbor in adj[curr]:
        if not visited[neighbor]:
            dfs(neighbor, visited, result)

    return result


if __name__ == "__main__":
    add_edge(0, 1)  # P - I
    add_edge(0, 2)  # P - O
    add_edge(0, 3)  # P - D
    add_edge(1, 4)  # I - O
    add_edge(2, 5)  # O - S

    bfs(0)
    dfs_result = dfs(0)
    print("Graph DFS:", " - ".join(dfs_result))