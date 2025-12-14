class StaticArray:
    def __init__(self, cap=100):
        # O(n) - создаем массив размером cap, инициализируя все элементы None
        self.cap, self.data, self.size = cap, [None] * cap, 0

    def push_back(self, v):  # O(1) - константная сложность
        if self.size >= self.cap: raise IndexError("Full")  # O(1)
        self.data[self.size], self.size = v, self.size + 1  # O(1) - две операции присваивания

    def push_front(self, v):  # O(n) - линейная сложность
        if self.size >= self.cap: raise IndexError("Full")  # O(1)
        # O(n) - цикл выполняется size раз (сдвиг всех элементов)
        for i in range(self.size, 0, -1):
            self.data[i] = self.data[i - 1]  # O(1) внутри цикла
        self.data[0], self.size = v, self.size + 1  # O(1)

    def insert(self, i, v):  # O(n) - линейная сложность
        if i < 0 or i > self.size: raise IndexError("Bad index")  # O(1)
        if i == self.size:
            return self.push_back(v)  # O(1) в этом случае
        # O(n) - цикл выполняется (size - i) раз
        for j in range(self.size, i, -1):
            self.data[j] = self.data[j - 1]  # O(1) внутри цикла
        self.data[i], self.size = v, self.size + 1  # O(1)

    def remove(self, i):  # O(n) - линейная сложность
        if i < 0 or i >= self.size: raise IndexError("Bad index")  # O(1)
        # O(n) - цикл выполняется (size - i - 1) раз
        for j in range(i, self.size - 1):
            self.data[j] = self.data[j + 1]  # O(1) внутри цикла
        self.data[self.size - 1], self.size = None, self.size - 1  # O(1)

    def find(self, v):  # O(n) - линейная сложность
        # O(n) - в худшем случае проходим все size элементов
        for i in range(self.size):  # size итераций
            if self.data[i] == v: return i  # O(1) сравнение
        return -1  # O(1)

    def __str__(self):  # O(n) - линейная сложность
        # O(n) - генератор проходит все size элементов
        return f"[{', '.join(str(self.data[i]) for i in range(self.size))}]"

    def __len__(self):  # O(1) - константная сложность
        return self.size  # O(1) - просто возврат значения

# Демо
arr = StaticArray(8)
arr.push_back(10);
arr.push_back(20);
arr.push_back(30)
print(f"После push_back: {arr}")
arr.push_front(99)
print(f"После push_front(99): {arr}")
arr.insert(2, 777)
print(f"После insert(2, 777): {arr}")
print(f"Найти 777: {arr.find(777)}")
arr.remove(1)
print(f"После remove(1): {arr}")
print(f"Размер: {len(arr)}")