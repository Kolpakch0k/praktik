class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        """Вставка узла"""
        if not self.root:
            self.root = Node(val)
            return

        curr = self.root
        while True:
            if val < curr.val:
                if curr.left is None:
                    curr.left = Node(val)
                    return
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = Node(val)
                    return
                curr = curr.right

    def search(self, val):
        """Поиск значения"""
        curr = self.root
        while curr:
            if val == curr.val:
                return True
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def delete(self, val):
        """Удаление узла"""
        self.root = self._delete(self.root, val)

    def _delete(self, node, val):
        if not node:
            return None

        if val < node.val:
            node.left = self._delete(node.left, val)
        elif val > node.val:
            node.right = self._delete(node.right, val)
        else:
            # Нашли узел для удаления
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            else:
                # У узла есть оба ребенка
                # Находим минимальный в правом поддереве
                min_node = self._find_min(node.right)
                node.val = min_node.val
                node.right = self._delete(node.right, min_node.val)

        return node

    def _find_min(self, node):
        while node.left:
            node = node.left
        return node

    # Обходы дерева
    def inorder(self):
        """Левый -> Корень -> Правый"""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.val)
            self._inorder(node.right, result)

    def preorder(self):
        """Корень -> Левый -> Правый"""
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.val)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):
        """Левый -> Правый -> Корень"""
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.val)

    def is_balanced(self):
        """Проверка сбалансированности"""
        return self._check_height(self.root) != -1

    def _check_height(self, node):
        if not node:
            return 0

        left_height = self._check_height(node.left)
        if left_height == -1:
            return -1

        right_height = self._check_height(node.right)
        if right_height == -1:
            return -1

        if abs(left_height - right_height) > 1:
            return -1

        return max(left_height, right_height) + 1

    def height(self):
        """Высота дерева"""
        return self._height(self.root)

    def _height(self, node):
        if not node:
            return 0
        return max(self._height(node.left), self._height(node.right)) + 1


# Демонстрация
print("=== БИНАРНОЕ ДЕРЕВО ПОИСКА (BST) ===\n")

# Создаем дерево
bst = BST()
values = [50, 30, 70, 20, 40, 60, 80]

print("1. Вставка значений:", values)
for val in values:
    bst.insert(val)

print("\n2. Обходы дерева:")
print("   In-order  (сортировка):", bst.inorder())
print("   Pre-order :", bst.preorder())
print("   Post-order:", bst.postorder())

print("\n3. Поиск значений:")
for val in [40, 55, 70]:
    found = bst.search(val)
    print(f"   Поиск {val}: {'Найден' if found else 'Не найден'}")

print("\n4. Высота дерева:", bst.height())
print("   Сбалансировано?:", "Да" if bst.is_balanced() else "Нет")

print("\n5. Удаление узла 30")
bst.delete(30)
print("   In-order после удаления:", bst.inorder())

print("\n6. Добавляем несбалансированное дерево:")
bst2 = BST()
for val in [10, 20, 30, 40, 50]:  # Это создаст "вырожденное" дерево
    bst2.insert(val)

print("   Значения:", bst2.inorder())
print("   Высота:", bst2.height())
print("   Сбалансировано?:", "Да" if bst2.is_balanced() else "Нет")

# Упрощенная версия
print("\n=== УПРОЩЕННАЯ ВЕРСИЯ ===")


class SimpleBST:
    def __init__(self):
        self.root = None

    def add(self, val):
        def _add(node, val):
            if not node:
                return Node(val)
            if val < node.val:
                node.left = _add(node.left, val)
            else:
                node.right = _add(node.right, val)
            return node

        self.root = _add(self.root, val)

    def inorder(self):
        def _inorder(node):
            return _inorder(node.left) + [node.val] + _inorder(node.right) if node else []

        return _inorder(self.root)

    def search(self, val):
        def _search(node, val):
            if not node:
                return False
            if val == node.val:
                return True
            return _search(node.left if val < node.val else node.right, val)

        return _search(self.root, val)


# Тест
simple = SimpleBST()
for v in [5, 3, 7, 2, 4]:
    simple.add(v)

print("Простое дерево:", simple.inorder())
print("Поиск 4:", simple.search(4))
print("Поиск 6:", simple.search(6))