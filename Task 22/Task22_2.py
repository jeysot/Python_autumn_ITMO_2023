def find_max_path_length(tree):
    def dfs(node, length):
        nonlocal max_length
        visited[node] = True
        max_length = max(max_length, length)

        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(neighbor, length + 1)

    graph = {}
    for edge in tree:
        if edge[0] not in graph:
            graph[edge[0]] = []
        if edge[1] not in graph:
            graph[edge[1]] = []
        graph[edge[0]].append(edge[1])
        graph[edge[1]].append(edge[0])


    visited = [False] * (len(graph) + 1)
    max_length = 0

    dfs(1, 0)

    return max_length


tree_structure = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (6, 7), (7, 8)]
result = find_max_path_length(tree_structure)
print("Максимальная длина пути от вершины (1) до конечной вершины:", result)
