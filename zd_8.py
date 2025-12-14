class HashTable:
    """Хэш-таблица с цепочками"""

    def __init__(self, size=7):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        """Хэш-функция для строк"""
        h = 0
        for char in str(key):
            h = (h * 31 + ord(char)) % self.size
        return h

    def put(self, key, value):
        """Добавление/обновление ключа-значения"""
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)  # Обновить
                return
        self.table[idx].append((key, value))  # Добавить новый

    def get(self, key):
        """Получение значения по ключу"""
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def remove(self, key):
        """Удаление ключа"""
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                del self.table[idx][i]
                return True
        return False

    def __str__(self):
        """Визуализация таблицы"""
        result = []
        for i in range(self.size):
            if self.table[i]:
                chain = " → ".join(f"'{k}':{v}" for k, v in self.table[i])
                result.append(f"[{i}] {chain}")
            else:
                result.append(f"[{i}] ∅")
        return "\n".join(result)


# Демонстрация
print("=== ХЭШ-ТАБЛИЦА С ЦЕПОЧКАМИ ===\n")

# Создаем таблицу
ht = HashTable(7)
print("Создана пустая таблица:")
print(ht)

# Добавляем элементы
print("\n1. Добавляем элементы:")
items = [
    ("apple", 10),
    ("banana", 20),
    ("orange", 30),
    ("grape", 40),
    ("kiwi", 50),
    ("melon", 60),
    ("pear", 70),
    ("apple", 99)  # Обновление существующего
]

for key, value in items:
    ht.put(key, value)
    print(f"  put('{key}', {value})")

print("\nТекущее состояние таблицы:")
print(ht)

# Поиск элементов
print("\n2. Поиск элементов:")
test_keys = ["banana", "kiwi", "mango"]
for key in test_keys:
    value = ht.get(key)
    print(f"  get('{key}') = {value}")

# Удаление
print("\n3. Удаление элементов:")
ht.remove("orange")
ht.remove("grape")
print("  remove('orange'), remove('grape')")
print("\nПосле удаления:")
print(ht)

# Коллизии
print("\n4. Демонстрация коллизий:")
print("  Хэш-функция для 'cat':", ht._hash("cat"))
print("  Хэш-функция для 'dog':", ht._hash("dog"))
print("  Хэш-функция для 'bird':", ht._hash("bird"))

# Минимальная версия
print("\n=== УПРОЩЕННАЯ ВЕРСИЯ ===")


class MiniHashTable:
    def __init__(self, sz=5):
        self.sz, self.t = sz, [[] for _ in range(sz)]

    def h(self, k):
        return sum(ord(c) for c in str(k)) % self.sz

    def put(self, k, v):
        idx = self.h(k)
        for i, (key, val) in enumerate(self.t[idx]):
            if key == k:
                self.t[idx][i] = (k, v);
                return
        self.t[idx].append((k, v))

    def get(self, k):
        for key, val in self.t[self.h(k)]:
            if key == k: return val
        return None

    def __str__(self):
        return '\n'.join(f"{i}:{b}" for i, b in enumerate(self.t))


# Быстрый тест
mht = MiniHashTable()
mht.put("a", 1);
mht.put("b", 2);
mht.put("c", 3)
print("\nМини-таблица:")
print(mht)
print("get('a'):", mht.get("a"))
print("get('x'):", mht.get("x"))

# Сравнение методов разрешения коллизий
print("\n=== МЕТОДЫ РАЗРЕШЕНИЯ КОЛЛИЗИЙ ===")
print("""
ЦЕПОЧКИ:
  + Простая реализация
  + Автоматическое расширение
  - Доп. память на указатели

ОТКРЫТАЯ АДРЕСАЦИЯ:
  + Лучшая локальность кэша
  + Меньше аллокаций памяти
  - Сложнее с удалением
  - Может заполниться
""")

# Визуализация процесса
print("=== ПРОЦЕСС ХЭШИРОВАНИЯ ===")
test_word = "hello"
print(f"\nСлово: '{test_word}'")
print("Хэш-функция: (сумма кодов ASCII) % размер_таблицы")
ascii_sum = sum(ord(c) for c in test_word)
print(f"Сумма ASCII: {sum(ord(c) for c in test_word)}")
print(f"Размер таблицы: 7")
print(f"Хэш: {ascii_sum % 7}")