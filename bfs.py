visited = set()
def dfs(graph, visited, start):
    queue = [start]
    visited.add(start)

    while queue:
        node = queue.pop(0)
        for edge in graph[node]:
            if edge not in visited:
                queue.append(edge)
                visited.add(edge)


