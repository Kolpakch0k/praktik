# Решение через DFS
def count_islands_dfs(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0

    def dfs(r, c):
        # Выход за границы или вода (0) или уже посещено
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 0 or visited[r][c]:
            return

        visited[r][c] = True

        # Рекурсивно обходим соседей (4 направления)
        dfs(r + 1, c)  # вниз
        dfs(r - 1, c)  # вверх
        dfs(r, c + 1)  # вправо
        dfs(r, c - 1)  # влево

    for r in range(rows):
        for c in range(cols):
            # Если нашли землю и не посещали
            if grid[r][c] == 1 and not visited[r][c]:
                count += 1
                dfs(r, c)  # Обходим весь остров

    return count


# Решение через BFS
def count_islands_bfs(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    count = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and not visited[r][c]:
                count += 1

                # BFS для этого острова
                queue = [(r, c)]
                visited[r][c] = True

                while queue:
                    cr, cc = queue.pop(0)

                    # Проверяем 4 соседа
                    for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                        nr, nc = cr + dr, cc + dc

                        if (0 <= nr < rows and 0 <= nc < cols and
                                grid[nr][nc] == 1 and not visited[nr][nc]):
                            visited[nr][nc] = True
                            queue.append((nr, nc))

    return count


# Демонстрация
print("=== ЗАДАЧА 'ОСТРОВА' ===\n")

# Тестовые данные
test_grids = [
    # Один остров
    [[1, 1, 0, 0, 0],
     [1, 1, 0, 0, 0],
     [0, 0, 0, 1, 1],
     [0, 0, 0, 1, 1]],

    # Несколько островов
    [[1, 0, 1, 0, 1],
     [0, 1, 0, 1, 0],
     [1, 0, 1, 0, 1],
     [0, 1, 0, 1, 0]],

    # Нет островов
    [[0, 0, 0],
     [0, 0, 0],
     [0, 0, 0]],

    # Один большой остров
    [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]],
]

# Тестируем оба алгоритма
for i, grid in enumerate(test_grids, 1):
    print(f"Тест {i}:")

    # Печатаем сетку
    for row in grid:
        print("  ", " ".join(str(x) for x in row))

    dfs_result = count_islands_dfs(grid)
    bfs_result = count_islands_bfs(grid)

    print(f"  DFS: {dfs_result} островов")
    print(f"  BFS: {bfs_result} островов")
    print(f"  Совпали: {dfs_result == bfs_result}\n")


# Упрощенная версия (самая компактная)
def islands(grid):
    if not grid: return 0

    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0

    def dfs(r, c):
        if (r < 0 or r >= rows or c < 0 or c >= cols or
                grid[r][c] == 0 or (r, c) in visited):
            return

        visited.add((r, c))
        dfs(r + 1, c);
        dfs(r - 1, c);
        dfs(r, c + 1);
        dfs(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r, c) not in visited:
                count += 1
                dfs(r, c)

    return count


# Тест упрощенной версии
print("=== УПРОЩЕННАЯ ВЕРСИЯ ===")
simple_grid = [[1, 1, 0],
               [0, 1, 0],
               [0, 0, 1]]

print("Сетка:")
for row in simple_grid:
    print(" ", row)

result = islands(simple_grid)
print(f"Островов: {result}")


# Алгоритм без visited (изменяем исходную сетку)
def islands_inplace(grid):
    if not grid: return 0

    rows, cols = len(grid), len(grid[0])
    count = 0

    def sink(r, c):
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
            grid[r][c] = 0  # "Топим" остров
            sink(r + 1, c);
            sink(r - 1, c);
            sink(r, c + 1);
            sink(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                count += 1
                sink(r, c)

    return count


# Тест in-place алгоритма
print("\n=== IN-PLACE АЛГОРИТМ ===")
grid_copy = [row[:] for row in simple_grid]  # Копия для теста
print("До:", grid_copy)
print("Островов:", islands_inplace(grid_copy))
print("После:", grid_copy)