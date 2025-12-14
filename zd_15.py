class MinHeap:
    def __init__(self, array=None):
        self.heap = []
        if array:
            self.heap = array[:]
            self._heapify()

    def push(self, val):
        """Вставка элемента"""
        self.heap.append(val)
        self._sift_up(len(self.heap) - 1)

    def pop(self):
        """Извлечение минимума"""
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        # Меняем корень с последним элементом
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sift_down(0)

        return root

    def peek(self):
        """Просмотр минимума"""
        return self.heap[0] if self.heap else None

    def _heapify(self):
        """Построение кучи из массива"""
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self._sift_down(i)

    def _sift_up(self, i):
        """Просеивание вверх"""
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] < self.heap[parent]:
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

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str(self.heap)


# Демонстрация
print("=== МИН-КУЧА (MIN-HEAP) ===")

# 1. Построение кучи из массива
print("\n1. Построение кучи из массива [9, 5, 7, 2, 3, 6]:")
arr = [9, 5, 7, 2, 3, 6]
heap = MinHeap(arr)
print(f"   Результат: {heap}")

# 2. Вставка элементов
print("\n2. Вставка элементов 1 и 4:")
heap.push(1)
heap.push(4)
print(f"   После вставок: {heap}")

# 3. Извлечение минимума
print("\n3. Извлечение минимумов:")
print(f"   Минимум: {heap.peek()}")
for i in range(3):
    val = heap.pop()
    print(f"   Извлекли {val}, куча: {heap}")

# 4. Еще пример
print("\n4. Новая куча из пустого массива:")
heap2 = MinHeap()
for val in [10, 20, 5, 15, 30, 3]:
    heap2.push(val)
    print(f"   push({val}) -> {heap2}")

print("\n5. Извлечение всех элементов по порядку:")
while len(heap2) > 0:
    print(f"   pop() -> {heap2.pop()}")

# Упрощенная версия
print("\n=== УПРОЩЕННАЯ ВЕРСИЯ ===")


class SimpleHeap:
    def __init__(self):
        self.h = []

    def add(self, x):
        self.h.append(x)
        i = len(self.h) - 1
        # Просеивание вверх
        while i > 0 and self.h[i] < self.h[(i - 1) // 2]:
            self.h[i], self.h[(i - 1) // 2] = self.h[(i - 1) // 2], self.h[i]
            i = (i - 1) // 2

    def get_min(self):
        if not self.h: return None
        return self.h[0]

    def extract(self):
        if not self.h: return None
        if len(self.h) == 1: return self.h.pop()

        res = self.h[0]
        self.h[0] = self.h.pop()
        i, n = 0, len(self.h)

        # Просеивание вниз
        while True:
            small = i
            l, r = 2 * i + 1, 2 * i + 2

            if l < n and self.h[l] < self.h[small]:
                small = l
            if r < n and self.h[r] < self.h[small]:
                small = r

            if small == i: break

            self.h[i], self.h[small] = self.h[small], self.h[i]
            i = small

        return res

    def __str__(self):
        return str(self.h)


# Тест
sh = SimpleHeap()
for x in [5, 2, 8, 1, 3]:
    sh.add(x)
print(f"Куча после добавок: {sh}")
print(f"Минимум: {sh.get_min()}")
print(f"Извлекли: {sh.extract()}")
print(f"Куча после извлечения: {sh}")