from collections import deque


# 1. Хранение графов
class Graph:
    def __init__(self, n, use_matrix=True):
        self.n = n
        self.use_matrix = use_matrix
        if use_matrix:
            self.data = [[0] * n for _ in range(n)]
        else:
            self.data = [[] for _ in range(n)]

    def add_edge(self, u, v, directed=False):
        if self.use_matrix:
            self.data[u][v] = 1
            if not directed:
                self.data[v][u] = 1
        else:
            self.data[u].append(v)
            if not directed:
                self.data[v].append(u)

    def get_neighbors(self, v):
        if self.use_matrix:
            return [i for i in range(self.n) if self.data[v][i]]
        else:
            return self.data[v]

    def __str__(self):
        if self.use_matrix:
            return "\n".join(" ".join(str(x) for x in row) for row in self.data)
        else:
            return "\n".join(f"{i}: {neighbors}" for i, neighbors in enumerate(self.data))


# 2. BFS (Поиск в ширину)
def bfs(graph, start):
    visited = [False] * graph.n
    queue = deque([start])
    visited[start] = True
    result = []

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph.get_neighbors(vertex):
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)

    return result


# 3. DFS (Поиск в глубину)
def dfs(graph, start):
    visited = [False] * graph.n
    result = []

    def dfs_recursive(v):
        visited[v] = True
        result.append(v)
        for neighbor in graph.get_neighbors(v):
            if not visited[neighbor]:
                dfs_recursive(neighbor)

    dfs_recursive(start)
    return result


# 4. Поиск кратчайшего пути в невзвешенном графе (BFS)
def shortest_path(graph, start, end):
    if start == end:
        return [start]

    visited = [False] * graph.n
    parent = [-1] * graph.n
    queue = deque([start])
    visited[start] = True

    while queue:
        vertex = queue.popleft()

        for neighbor in graph.get_neighbors(vertex):
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = vertex
                queue.append(neighbor)

                if neighbor == end:
                    # Восстанавливаем путь
                    path = []
                    cur = end
                    while cur != -1:
                        path.append(cur)
                        cur = parent[cur]
                    return path[::-1]

    return []  # Путь не найден


# Демонстрация
print("=== ГРАФЫ И АЛГОРИТМЫ ===\n")

# Создаем граф
n = 7
g = Graph(n, use_matrix=False)

# Граф в виде сетки 3x3 (0-1-2 в первой строке, 3-4-5 во второй, 6 внизу)
edges = [(0, 1), (1, 2), (0, 3), (1, 4), (2, 5), (3, 4), (4, 5), (3, 6), (5, 6)]
for u, v in edges:
    g.add_edge(u, v)

print("1. Граф (список смежности):")
print(g)

print("\n2. BFS обход (начиная с 0):")
bfs_result = bfs(g, 0)
print("   Порядок обхода:", bfs_result)

print("\n3. DFS обход (начиная с 0):")
dfs_result = dfs(g, 0)
print("   Порядок обхода:", dfs_result)

print("\n4. Кратчайший путь от 0 до 6:")
path = shortest_path(g, 0, 6)
if path:
    print(f"   Путь: {' → '.join(map(str, path))}")
    print(f"   Длина: {len(path) - 1}")
else:
    print("   Путь не найден")

print("\n5. Матрица смежности того же графа:")
g_matrix = Graph(n, use_matrix=True)
for u, v in edges:
    g_matrix.add_edge(u, v)
print(g_matrix)

# Упрощенная версия
print("\n=== УПРОЩЕННЫЕ АЛГОРИТМЫ ===")


class SimpleGraph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def add(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

    def bfs_simple(self, start):
        visited = [False] * self.n
        q = [start]
        visited[start] = True
        order = []

        while q:
            v = q.pop(0)
            order.append(v)
            for nb in self.adj[v]:
                if not visited[nb]:
                    visited[nb] = True
                    q.append(nb)
        return order

    def dfs_simple(self, start):
        visited = [False] * self.n
        stack = [start]
        order = []

        while stack:
            v = stack.pop()
            if not visited[v]:
                visited[v] = True
                order.append(v)
                for nb in reversed(self.adj[v]):  # Для правильного порядка
                    if not visited[nb]:
                        stack.append(nb)
        return order


# Тест
sg = SimpleGraph(5)
sg.add(0, 1);
sg.add(0, 2);
sg.add(1, 3);
sg.add(1, 4)
print("Простой граф с 5 вершинами:")
print("BFS от 0:", sg.bfs_simple(0))
print("DFS от 0:", sg.dfs_simple(0))