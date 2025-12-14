class TrieNode:
    def __init__(self):
        self.children = {}
        self.freq = 0  # Частота слова
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, freq=1):
        """Вставка слова с частотой"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
        node.freq += freq

    def autocomplete(self, prefix):
        """Поиск слов по префиксу"""
        # Находим узел префикса
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        # Собираем все слова с этого узла
        results = []
        stack = [(node, prefix)]

        while stack:
            curr_node, curr_word = stack.pop()
            if curr_node.is_end:
                results.append((curr_word, curr_node.freq))

            for char, child_node in curr_node.children.items():
                stack.append((child_node, curr_word + char))

        # Сортируем по частоте (убывание)
        results.sort(key=lambda x: x[1], reverse=True)
        return [word for word, freq in results]


# Комбинированная система: HashMap + Trie
class SmartDictionary:
    def __init__(self):
        self.trie = Trie()
        self.word_freq = {}  # HashMap для быстрого доступа к частотам

    def add_word(self, word, freq=1):
        """Добавление слова"""
        self.word_freq[word] = self.word_freq.get(word, 0) + freq
        self.trie.insert(word, freq)

    def add_text(self, text):
        """Добавление всех слов из текста"""
        import re
        words = re.findall(r'\w+', text.lower())
        for word in words:
            self.add_word(word)

    def autocomplete(self, prefix, limit=5):
        """Автодополнение по префиксу с учетом частоты"""
        words = self.trie.autocomplete(prefix)
        return words[:limit]

    def get_freq(self, word):
        """Получение частоты слова"""
        return self.word_freq.get(word, 0)


# Демонстрация
def main():
    print("=== TRIE + HASHMAP ДЛЯ АВТОДОПОЛНЕНИЯ ===\n")

    # Создаем словарь
    sd = SmartDictionary()

    # Добавляем слова с разными частотами
    words_with_freq = [
        ("apple", 50),
        ("app", 30),
        ("application", 20),
        ("apply", 10),
        ("banana", 40),
        ("band", 25),
        ("bandage", 5),
        ("cat", 60),
        ("car", 45),
        ("card", 35),
        ("carrot", 15),
    ]

    print("1. Добавляем слова:")
    for word, freq in words_with_freq:
        sd.add_word(word, freq)
        print(f"   '{word}': частота {freq}")

    # Тестируем автодополнение
    print("\n2. Тестируем автодополнение:")

    test_prefixes = ["app", "ba", "car", "z"]
    for prefix in test_prefixes:
        suggestions = sd.autocomplete(prefix)
        if suggestions:
            print(f"   '{prefix}' -> {suggestions}")
        else:
            print(f"   '{prefix}' -> нет совпадений")

    # Показываем частоты
    print("\n3. Частоты слов:")
    for word in ["apple", "app", "application"]:
        print(f"   '{word}': {sd.get_freq(word)}")

    # Работа с текстом
    print("\n4. Обработка текста:")
    text = "яблоко яблоко груша яблоко банан груша"
    sd2 = SmartDictionary()
    sd2.add_text(text)

    print(f"   Текст: '{text}'")
    print(f"   'яблоко': частота {sd2.get_freq('яблоко')}")
    print(f"   'груша': частота {sd2.get_freq('груша')}")
    print(f"   'банан': частота {sd2.get_freq('банан')}")


# Упрощенная версия
class SimpleTrie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        node['#'] = True  # Конец слова

    def search(self, prefix):
        """Поиск слов по префиксу"""
        # Находим узел префикса
        node = self.root
        for char in prefix:
            if char not in node:
                return []
            node = node[char]

        # DFS для поиска всех слов
        results = []
        stack = [(node, prefix)]

        while stack:
            curr_node, curr_word = stack.pop()
            if '#' in curr_node:
                results.append(curr_word)

            for char, child in curr_node.items():
                if char != '#':
                    stack.append((child, curr_word + char))

        return results


# Быстрый тест
print("\n=== УПРОЩЕННАЯ TRIE ===")
t = SimpleTrie()
for word in ["cat", "car", "card", "dog"]:
    t.insert(word)

print("Слова с префиксом 'ca':", t.search("ca"))
print("Слова с префиксом 'd':", t.search("d"))
print("Слова с префиксом 'x':", t.search("x"))

if __name__ == "__main__":
    main()