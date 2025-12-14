class Node:
    def __init__(self, val):
        self.val, self.next = val, None


class SinglyLinkedList:
    def __init__(self):
        self.head, self.size = None, 0

    # O(1) - всегда быстро
    def push_front(self, val):
        new = Node(val)
        new.next, self.head, self.size = self.head, new, self.size + 1

    # O(n) - нужно дойти до конца
    def push_back(self, val):
        new = Node(val)
        if not self.head:
            self.head = new
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new
        self.size += 1

    # O(n) - линейный поиск
    def find(self, val):
        cur, idx = self.head, 0
        while cur:
            if cur.val == val:
                return idx
            cur, idx = cur.next, idx + 1
        return -1

    # O(n) - поиск + удаление
    def remove(self, val):
        if not self.head:
            return False

        if self.head.val == val:
            self.head, self.size = self.head.next, self.size - 1
            return True

        cur = self.head
        while cur.next and cur.next.val != val:
            cur = cur.next

        if cur.next:
            cur.next, self.size = cur.next.next, self.size - 1
            return True

        return False

    # O(n) - проход по всем узлам
    def reverse(self):
        prev, cur = None, self.head
        while cur:
            nxt = cur.next
            cur.next, prev, cur = prev, cur, nxt
        self.head = prev

    def __str__(self):
        res, cur = [], self.head
        while cur:
            res.append(str(cur.val))
            cur = cur.next
        return "->".join(res) if res else "Пусто"

    def __len__(self):
        return self.size


# Оптимизированный список с хвостом
class FastList(SinglyLinkedList):
    def __init__(self):
        super().__init__()
        self.tail = None

    # O(1)
    def push_back(self, val):
        new = Node(val)
        if not self.head:
            self.head = self.tail = new
        else:
            self.tail.next, self.tail = new, new
        self.size += 1


# Сравнение операций
print("=== СРАВНЕНИЕ ОПЕРАЦИЙ ===")
print("\nВставка в начало:")
print("  Список: O(1) - просто создать узел")
print("  Массив: O(n) - сдвигать все элементы")

print("\nВставка в конец:")
print("  Список: O(n) - идти до конца")
print("  Список(с tail): O(1) - есть указатель на конец")
print("  Массив: O(1) - если есть место")

print("\nУдаление по значению:")
print("  Список: O(n) - найти + удалить")
print("  Массив: O(n) - найти + сдвинуть")

print("\nПоиск по значению:")
print("  Список: O(n) - линейный поиск")
print("  Массив: O(n) - линейный поиск")

# Демо
print("\n=== ДЕМО ===")
lst = SinglyLinkedList()
lst.push_front(3);
lst.push_front(2);
lst.push_front(1)
print(f"После push_front 3,2,1: {lst}")

lst.push_back(4);
lst.push_back(5)
print(f"После push_back 4,5: {lst}")

print(f"Найти 2: {lst.find(2)}")
print(f"Найти 99: {lst.find(99)}")

lst.remove(2)
print(f"После удаления 2: {lst}")

lst.reverse()
print(f"После разворота: {lst}")