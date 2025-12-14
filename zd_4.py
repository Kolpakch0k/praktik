class Node:
    def __init__(self, val):
        self.val, self.prev, self.next = val, None, None


class DoublyLinkedList:
    def __init__(self):
        self.head, self.tail, self.size = None, None, 0

    def push_back(self, val):  # O(1)
        n = Node(val)
        if not self.head:
            self.head = self.tail = n
        else:
            self.tail.next, n.prev, self.tail = n, self.tail, n
        self.size += 1

    def push_front(self, val):  # O(1)
        n = Node(val)
        if not self.head:
            self.head = self.tail = n
        else:
            self.head.prev, n.next, self.head = n, self.head, n
        self.size += 1

    def insert_after(self, node, val):  # O(1) - узел уже есть
        if not node: return
        n = Node(val)
        n.prev, n.next = node, node.next
        if node.next: node.next.prev = n
        node.next = n
        if node == self.tail: self.tail = n
        self.size += 1

    def delete_node(self, node):  # O(1) - узел уже есть
        if not node: return False
        if node.prev: node.prev.next = node.next
        if node.next: node.next.prev = node.prev
        if node == self.head: self.head = node.next
        if node == self.tail: self.tail = node.prev
        self.size -= 1
        return True

    def find(self, val):  # O(n)
        cur = self.head
        while cur:
            if cur.val == val:
                return cur
            cur = cur.next
        return None

    # Итератор
    def __iter__(self):
        cur = self.head
        while cur:
            yield cur.val
            cur = cur.next

    def __str__(self):
        return "↔".join(str(x) for x in self) if self.size else "[]"


# Итератор по узлам (для вставки/удаления)
class NodeIterator:
    def __init__(self, dll):
        self.cur = dll.head

    def __iter__(self):
        return self

    def __next__(self):
        if not self.cur:
            raise StopIteration
        node = self.cur
        self.cur = self.cur.next
        return node


# Демо
dll = DoublyLinkedList()
for i in range(1, 4):
    dll.push_back(i)
print(f"Создали: {dll}")

# Вставка после найденного узла
node = dll.find(2)
if node:
    dll.insert_after(node, 99)
print(f"Вставили 99 после 2: {dll}")

# Удаление узла без поиска (O(1))
node = dll.find(99)
if node:
    dll.delete_node(node)
print(f"Удалили 99: {dll}")

# Итерация
print("Итерация:", list(dll))