# Очередь на циклическом массиве
class CircularQueue:
    def __init__(self, capacity=10):
        self.cap = capacity
        self.data = [None] * capacity
        self.front = 0  # Индекс первого элемента
        self.rear = 0  # Индекс для следующего элемента
        self.size = 0

    def enqueue(self, x):  # O(1)
        """Добавление в конец очереди"""
        if self.is_full():
            raise Exception("Очередь переполнена")

        self.data[self.rear] = x
        self.rear = (self.rear + 1) % self.cap  # Циклический сдвиг
        self.size += 1

    def dequeue(self):  # O(1)
        """Удаление из начала очереди"""
        if self.is_empty():
            raise Exception("Очередь пуста")

        val = self.data[self.front]
        self.front = (self.front + 1) % self.cap  # Циклический сдвиг
        self.size -= 1
        return val

    def peek(self):  # O(1)
        """Просмотр первого элемента"""
        if self.is_empty():
            return None
        return self.data[self.front]

    def is_empty(self):  # O(1)
        return self.size == 0

    def is_full(self):  # O(1)
        return self.size == self.cap

    def __len__(self):  # O(1)
        return self.size

    def __str__(self):
        """Визуализация циклической очереди"""
        result = []
        for i in range(self.size):
            idx = (self.front + i) % self.cap
            result.append(str(self.data[idx]))
        return "->".join(result) if result else "Пусто"


# Очередь на двух стеках
class TwoStackQueue:
    def __init__(self):
        self.stack_in = []  # Для добавления элементов
        self.stack_out = []  # Для удаления элементов
        self.size = 0

    def enqueue(self, x):  # O(1)
        """Добавление в очередь"""
        self.stack_in.append(x)
        self.size += 1

    def dequeue(self):  # O(n) в худшем случае, O(1) амортизированно
        """Удаление из очереди"""
        if self.is_empty():
            raise Exception("Очередь пуста")

        # Если stack_out пуст, переливаем все из stack_in
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        self.size -= 1
        return self.stack_out.pop()

    def peek(self):  # O(n) в худшем случае, O(1) амортизированно
        """Просмотр первого элемента"""
        if self.is_empty():
            return None

        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        return self.stack_out[-1]

    def is_empty(self):  # O(1)
        return self.size == 0

    def __len__(self):  # O(1)
        return self.size

    def __str__(self):
        """Визуализация очереди на двух стеках"""
        # Показываем элементы в порядке очереди
        temp = []
        # Сначала элементы из stack_out (в обратном порядке)
        for i in range(len(self.stack_out) - 1, -1, -1):
            temp.append(str(self.stack_out[i]))
        # Затем элементы из stack_in (в прямом порядке)
        temp.extend(str(x) for x in self.stack_in)
        return "->".join(temp) if temp else "Пусто"


# Демонстрация
print("=== ОЧЕРЕДЬ НА ЦИКЛИЧЕСКОМ МАССИВЕ ===")
cq = CircularQueue(5)
print(f"Создана очередь емкостью 5")

for i in range(1, 6):
    cq.enqueue(i * 10)
    print(f"enqueue({i * 10}): {cq}")

print(f"\npeek: {cq.peek()}")
print(f"dequeue: {cq.dequeue()}, осталось: {cq}")
print(f"dequeue: {cq.dequeue()}, осталось: {cq}")

cq.enqueue(60)
print(f"enqueue(60): {cq}")
cq.enqueue(70)
print(f"enqueue(70): {cq}")
print(f"Размер: {len(cq)}, полная? {cq.is_full()}")

print("\n=== ОЧЕРЕДЬ НА ДВУХ СТЕКАХ ===")
tsq = TwoStackQueue()
print("Создана очередь на двух стеках")

for i in range(1, 6):
    tsq.enqueue(i)
    print(f"enqueue({i}): stack_in={tsq.stack_in}, stack_out={tsq.stack_out}")

print(f"\npeek: {tsq.peek()}")
print(f"dequeue: {tsq.dequeue()}")
print(f"Состояние: stack_in={tsq.stack_in}, stack_out={tsq.stack_out}")
print(f"dequeue: {tsq.dequeue()}")
print(f"Очередь: {tsq}")

tsq.enqueue(6)
tsq.enqueue(7)
print(f"\nenqueue(6), enqueue(7)")
print(f"Очередь: {tsq}")
print(f"Размер: {len(tsq)}")

# Сравнение сложности
print("\n=== СРАВНЕНИЕ СЛОЖНОСТИ ===")
print("Циклический массив:")
print("  enqueue: O(1)")
print("  dequeue: O(1)")
print("  peek: O(1)")
print("\nДва стека:")
print("  enqueue: O(1)")
print("  dequeue: O(n) худший, O(1) амортизированно")
print("  peek: O(n) худший, O(1) амортизированно")
print("\nПочему два стека работают?")
print("  В худшем случае при пустом stack_out")
print("  переливаем все элементы из stack_in: O(n)")
print("  Но это происходит редко, в среднем O(1)")

# Пример использования
print("\n=== ПРИМЕР ИСПОЛЬЗОВАНИЯ ===")
# Моделирование очереди задач
print("Очередь задач на печать:")
queue = TwoStackQueue()  # Или CircularQueue

tasks = ["doc1.pdf", "doc2.pdf", "report.docx"]
for task in tasks:
    queue.enqueue(task)
    print(f"Добавлена задача: {task}")

print("\nОбработка задач:")
while not queue.is_empty():
    task = queue.dequeue()
    print(f"Печатается: {task}")
    print(f"Осталось задач: {len(queue)}")