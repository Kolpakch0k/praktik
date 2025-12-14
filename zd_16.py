class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, value, priority):
        """Добавление элемента с приоритетом"""
        self.heap.append((priority, value))
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        """Извлечение элемента с минимальным приоритетом"""
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()[1]

        # Берем корень (минимальный приоритет)
        priority, value = self.heap[0]

        # Заменяем корень последним элементом
        self.heap[0] = self.heap.pop()
        self._sift_down(0)

        return value

    def peek(self):
        """Просмотр элемента с минимальным приоритетом"""
        return self.heap[0][1] if self.heap else None

    def _sift_up(self, i):
        """Просеивание вверх"""
        parent = (i - 1) // 2
        while i > 0 and self.heap[i][0] < self.heap[parent][0]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def _sift_down(self, i):
        """Просеивание вниз"""
        n = len(self.heap)
        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self.heap[left][0] < self.heap[smallest][0]:
                smallest = left

            if right < n and self.heap[right][0] < self.heap[smallest][0]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str([f"{v}({p})" for p, v in self.heap])


# 1. Планирование задач
def task_scheduling():
    print("=== ПЛАНИРОВАНИЕ ЗАДАЧ ===")

    pq = PriorityQueue()

    # Добавляем задачи с приоритетами (меньше = выше приоритет)
    tasks = [
        ("Отправить отчет", 3),
        ("Подготовить презентацию", 1),
        ("Ответить на email", 2),
        ("Созвониться с клиентом", 1),
        ("Проверить код", 4)
    ]

    print("Добавляем задачи:")
    for task, priority in tasks:
        pq.push(task, priority)
        print(f"  push('{task}', приоритет={priority})")

    print(f"\nОчередь: {pq}")

    print("\nВыполняем задачи по приоритету:")
    while len(pq) > 0:
        task = pq.pop()
        print(f"  Выполняем: {task}")


# 2. Поиск k минимальных элементов
def k_smallest(arr, k):
    """Поиск k минимальных элементов"""
    if k <= 0:
        return []

    # Создаем кучу и добавляем первые k элементов
    heap = []
    for i in range(min(k, len(arr))):
        heap.append((-arr[i], i))  # Используем отрицательные значения для макс-кучи

    # Преобразуем в кучу
    for i in range(len(heap) // 2 - 1, -1, -1):
        _sift_down_max(heap, i)

    # Обрабатываем остальные элементы
    for i in range(k, len(arr)):
        if arr[i] < -heap[0][0]:  # arr[i] < текущего максимума в куче
            heap[0] = (-arr[i], i)
            _sift_down_max(heap, 0)

    # Извлекаем k минимальных элементов
    result = [-priority for priority, _ in heap]
    result.sort()  # Сортируем для красивого вывода
    return result


def _sift_down_max(heap, i):
    """Просеивание вниз для макс-кучи"""
    n = len(heap)
    while True:
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and heap[left][0] > heap[largest][0]:
            largest = left

        if right < n and heap[right][0] > heap[largest][0]:
            largest = right

        if largest == i:
            break

        heap[i], heap[largest] = heap[largest], heap[i]
        i = largest


def test_k_smallest():
    print("\n=== ПОИСК K МИНИМАЛЬНЫХ ЭЛЕМЕНТОВ ===")

    arr = [10, 3, 7, 1, 9, 2, 8, 5, 4, 6]
    print(f"Массив: {arr}")

    for k in [1, 3, 5, 10]:
        result = k_smallest(arr, k)
        print(f"  {k} минимальных: {result}")


# Упрощенная версия PriorityQueue
class MinPQ:
    def __init__(self):
        self.h = []

    def add(self, val, prio):
        self.h.append((prio, val))
        i = len(self.h) - 1
        while i > 0 and self.h[i][0] < self.h[(i - 1) // 2][0]:
            self.h[i], self.h[(i - 1) // 2] = self.h[(i - 1) // 2], self.h[i]
            i = (i - 1) // 2

    def get(self):
        if not self.h: return None
        if len(self.h) == 1: return self.h.pop()[1]

        res = self.h[0][1]
        self.h[0] = self.h.pop()
        i, n = 0, len(self.h)

        while True:
            s = i
            l, r = 2 * i + 1, 2 * i + 2
            if l < n and self.h[l][0] < self.h[s][0]: s = l
            if r < n and self.h[r][0] < self.h[s][0]: s = r
            if s == i: break
            self.h[i], self.h[s] = self.h[s], self.h[i]
            i = s

        return res

    def __len__(self):
        return len(self.h)


# Демонстрация
if __name__ == "__main__":
    # Тестируем планирование задач
    task_scheduling()

    # Тестируем поиск k минимальных
    test_k_smallest()

    # Быстрый тест упрощенной PQ
    print("\n=== БЫСТРЫЙ ТЕСТ УПРОЩЕННОЙ PQ ===")
    pq = MinPQ()
    pq.add("Задача A", 2)
    pq.add("Задача B", 1)
    pq.add("Задача C", 3)
    print(f"Добавили 3 задачи")
    print(f"Выполняем: {pq.get()}")
    print(f"Выполняем: {pq.get()}")
    print(f"Выполняем: {pq.get()}")

    # Поиск k минимальных через heapq
    print("\n=== ПОИСК K МИНИМАЛЬНЫХ (через heapq) ===")
    import heapq


    def k_smallest_heapq(arr, k):
        return heapq.nsmallest(k, arr)


    arr = [10, 3, 7, 1, 9, 2, 8, 5, 4, 6]
    print(f"Массив: {arr}")
    print(f"3 минимальных (heapq): {k_smallest_heapq(arr, 3)}")