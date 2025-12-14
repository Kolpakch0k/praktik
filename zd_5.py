# Стек на массиве
class ArrayStack:
    def __init__(self):
        self.data = []

    def push(self, x):  # O(1)
        self.data.append(x)

    def pop(self):  # O(1)
        return self.data.pop() if self.data else None

    def peek(self):  # O(1)
        return self.data[-1] if self.data else None

    def is_empty(self):  # O(1)
        return len(self.data) == 0

    def __len__(self):  # O(1)
        return len(self.data)


# Стек на связном списке
class Node:
    def __init__(self, val):
        self.val, self.next = val, None


class ListStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, x):  # O(1)
        n = Node(x)
        n.next, self.top, self.size = self.top, n, self.size + 1

    def pop(self):  # O(1)
        if not self.top: return None
        val = self.top.val
        self.top, self.size = self.top.next, self.size - 1
        return val

    def peek(self):  # O(1)
        return self.top.val if self.top else None

    def is_empty(self):  # O(1)
        return self.top is None

    def __len__(self):
        return self.size


# Проверка скобок
def check_brackets(expr):
    """Проверка корректности скобочной последовательности"""
    stack = ArrayStack()  # Можно использовать любой стек
    pairs = {')': '(', ']': '[', '}': '{'}

    for ch in expr:
        if ch in '([{':  # Открывающая скобка
            stack.push(ch)
        elif ch in ')]}':  # Закрывающая скобка
            if stack.is_empty() or stack.pop() != pairs[ch]:
                return False

    return stack.is_empty()  # Все скобки должны быть закрыты


# Демо
print("=== ДЕМО СТЕКА ===")

# Тест ArrayStack
print("1. Стек на массиве:")
s1 = ArrayStack()
for i in [1, 2, 3]: s1.push(i)
print(f"   push 1,2,3: {s1.data}")
print(f"   pop: {s1.pop()}")
print(f"   peek: {s1.peek()}")
print(f"   size: {len(s1)}")

# Тест ListStack
print("\n2. Стек на списке:")
s2 = ListStack()
for i in [4, 5, 6]: s2.push(i)
print(f"   push 4,5,6")
print(f"   pop: {s2.pop()}")
print(f"   peek: {s2.peek()}")
print(f"   size: {len(s2)}")

# Проверка скобок
print("\n3. Проверка скобок:")
tests = [
    ("()", True),
    ("()[]{}", True),
    ("(]", False),
    ("([)]", False),
    ("{[]}", True),
    ("((()))", True),
    ("((())", False)
]

for expr, expected in tests:
    result = check_brackets(expr)
    status = "✓" if result == expected else "✗"
    print(f"   {status} '{expr}' -> {result} (ожидалось {expected})")

# Сложность операций
print("\n=== СЛОЖНОСТЬ ===")
print("Массив: push O(1)*, pop O(1), peek O(1)")
print("Список: push O(1), pop O(1), peek O(1)")
print("* - O(1) амортизированно для массива")