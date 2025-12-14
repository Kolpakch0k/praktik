class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.freq = 0  # Количество слов с этим префиксом


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Вставка слова"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.freq += 1
        node.is_end = True

    def search(self, word):
        """Поиск слова целиком"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def prefix_count(self, prefix):
        """Количество слов с данным префиксом"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.freq

    def delete(self, word):
        """Удаление слова"""
        if not self.search(word):
            return False

        node = self.root
        stack = []  # Для отслеживания пути

        for char in word:
            stack.append((node, char))
            node = node.children[char]

        # Помечаем конец слова как False
        node.is_end = False

        # Уменьшаем счетчики и удаляем узлы если нужно
        for parent, char in reversed(stack):
            child = parent.children[char]
            child.freq -= 1

            # Удаляем узел если у него нет детей и это не конец другого слова
            if child.freq == 0 and not child.is_end:
                del parent.children[char]

        return True

    def autocomplete(self, prefix):
        """Автодополнение по префиксу"""
        # Находим узел префикса
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        # Собираем все слова
        results = []
        stack = [(node, prefix)]

        while stack:
            curr_node, curr_word = stack.pop()
            if curr_node.is_end:
                results.append(curr_word)

            for char, child in curr_node.children.items():
                stack.append((child, curr_word + char))

        return results


# Демонстрация
print("=== РАСШИРЕННАЯ TRIE ===")

trie = Trie()
words = ["apple", "app", "application", "apply", "banana", "band"]

print("1. Вставляем слова:", words)
for word in words:
    trie.insert(word)

print("\n2. Поиск слов:")
for word in ["app", "apple", "appl", "ban"]:
    found = trie.search(word)
    print(f"   '{word}' -> {'Найдено' if found else 'Не найдено'}")

print("\n3. Подсчет по префиксу:")
prefixes = ["app", "b", "ban", "c"]
for prefix in prefixes:
    count = trie.prefix_count(prefix)
    print(f"   '{prefix}' -> {count} слов")

print("\n4. Автодополнение:")
for prefix in ["app", "ba"]:
    completions = trie.autocomplete(prefix)
    print(f"   '{prefix}' -> {completions}")

print("\n5. Удаление слова 'app'")
trie.delete("app")

print("   Поиск 'app':", trie.search("app"))
print("   Поиск 'apple':", trie.search("apple"))
print("   Префикс 'app':", trie.prefix_count("app"), "слов")

# Упрощенная версия
print("\n=== УПРОЩЕННАЯ TRIE ===")


class SimpleTrie:
    def __init__(self):
        self.root = {}

    def add(self, word):
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {'count': 0}
            node = node[c]
            node['count'] = node.get('count', 0) + 1
        node['#'] = True  # Конец слова

    def remove(self, word):
        node = self.root
        stack = []

        for c in word:
            if c not in node:
                return False
            stack.append((node, c))
            node = node[c]

        if '#' not in node:
            return False

        del node['#']

        for parent, char in reversed(stack):
            child = parent[char]
            child['count'] -= 1
            if child['count'] == 0 and '#' not in child:
                del parent[char]

        return True

    def prefix_words(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node:
                return 0
            node = node[c]
        return node.get('count', 0)


# Тест
st = SimpleTrie()
for w in ["cat", "car", "card"]:
    st.add(w)

print("Добавили: cat, car, card")
print("Префикс 'ca':", st.prefix_words("ca"), "слов")
print("Префикс 'car':", st.prefix_words("car"), "слов")

st.remove("car")
print("\nУдалили 'car'")
print("Префикс 'ca':", st.prefix_words("ca"), "слов")
print("Префикс 'car':", st.prefix_words("car"), "слов")