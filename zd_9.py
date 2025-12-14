import time
import re
from collections import defaultdict


# 1. Класс HashMap с разными хэш-функциями
class HashMap:
    def __init__(self, hash_func="good"):
        self.size = 1000
        self.table = [[] for _ in range(self.size)]
        self.hash_func = hash_func

    def _hash_good(self, key):
        """Хорошая хэш-функция"""
        h = 0
        for char in str(key):
            h = (h * 31 + ord(char)) % self.size
        return h

    def _hash_bad(self, key):
        """Плохая хэш-функция (всегда 1)"""
        return 1

    def _hash(self, key):
        if self.hash_func == "bad":
            return self._hash_bad(key)
        return self._hash_good(key)

    def put(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)
                return
        self.table[idx].append((key, value))

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return 0

    def items(self):
        items = []
        for bucket in self.table:
            for k, v in bucket:
                items.append((k, v))
        return items


# 2. Функция для построения частотного словаря
def build_freq_dict(text, hash_type="good"):
    """Строит частотный словарь слов из текста"""
    # Очистка текста: оставляем только буквы и пробелы
    text = re.sub(r'[^\w\s]', ' ', text.lower())
    words = text.split()

    # Создаем хэш-таблицу
    freq_dict = HashMap(hash_type)

    # Подсчет частот
    for word in words:
        current = freq_dict.get(word)
        freq_dict.put(word, current + 1)

    return freq_dict


# 3. Текст для анализа
sample_text = """
А я иду, шагаю по Москве
И я ещё пройти смогу
Солёный Тихий океан
И тундру, и тайгу
Над лодкой белый парус
И в горах разрыв
Я на земле живу
И пока я хожу по планете
Спокойно спят планеты
Я на земле живу
И пока я хожу по планете
Спокойно спят планеты
Я на земле живу
"""


# 4. Основная программа
def main():
    print("=== ЧАСТОТНЫЙ СЛОВАРЬ СЛОВ ===\n")

    # Строим словари с разными хэш-функциями
    print("1. Строим частотный словарь...")

    start = time.time()
    good_dict = build_freq_dict(sample_text, "good")
    good_time = time.time() - start

    start = time.time()
    bad_dict = build_freq_dict(sample_text, "bad")
    bad_time = time.time() - start

    # Получаем все слова и их частоты
    words_good = good_dict.items()
    words_bad = bad_dict.items()

    print(f"   Хорошая хэш-функция: {good_time:.5f} сек")
    print(f"   Плохая хэш-функция:  {bad_time:.5f} сек")
    print(f"   Разница: {bad_time / good_time:.1f} раз\n")

    # Сортируем по частоте (убывание)
    sorted_words = sorted(words_good, key=lambda x: x[1], reverse=True)

    # Выводим топ-10
    print("2. ТОП-10 самых частых слов:")
    print("-" * 25)
    print(f"{'Слово':<15} {'Частота':<8}")
    print("-" * 25)

    for i, (word, freq) in enumerate(sorted_words[:10], 1):
        print(f"{i:2}. {word:<15} {freq:<8}")

    # 5. Визуализация хэш-таблиц
    print("\n3. Визуализация хэш-таблиц:")
    print("\n   Хорошая хэш-функция (равномерное распределение):")
    good_buckets = [len(bucket) for bucket in good_dict.table]
    print(f"   Пустых ячеек: {good_buckets.count(0)}")
    print(f"   Максимальная длина цепочки: {max(good_buckets)}")

    print("\n   Плохая хэш-функция (все ключи в одной ячейке):")
    bad_buckets = [len(bucket) for bucket in bad_dict.table]
    print(f"   Пустых ячеек: {bad_buckets.count(0)}")
    print(f"   Максимальная длина цепочки: {max(bad_buckets)}")

    # 6. Объяснение разницы
    print("\n4. Почему так происходит:")
    print("""
    ХОРОШАЯ хэш-функция:
    - Равномерно распределяет ключи
    - Поиск O(1) в среднем
    - Короткие цепочки

    ПЛОХАЯ хэш-функция:
    - Все ключи в одной ячейке
    - Поиск O(n) в худшем случае
    - Одна длинная цепочка
    """)


# Минимальная версия (для быстрого теста)
def quick_test():
    print("\n=== БЫСТРЫЙ ТЕСТ ===")

    # Минимальный HashMap
    class MiniHM:
        def __init__(self, bad=False):
            self.t = [None] * 10
            self.bad = bad

        def h(self, k):
            return 1 if self.bad else sum(ord(c) for c in str(k)) % 10

        def put(self, k, v):
            idx = self.h(k)
            if self.t[idx] is None:
                self.t[idx] = []
            for i, (key, val) in enumerate(self.t[idx]):
                if key == k:
                    self.t[idx][i] = (k, v)
                    return
            self.t[idx].append((k, v))

        def stats(self):
            lens = [len(b) if b else 0 for b in self.t]
            return f"Цепочки: {lens}, Max: {max(lens)}"

    # Тест
    text = "а а а б б в г г г г д"
    words = text.split()

    hm_good = MiniHM(bad=False)
    hm_bad = MiniHM(bad=True)

    for word in words:
        hm_good.put(word, 1)
        hm_bad.put(word, 1)

    print("Хорошая хэш:", hm_good.stats())
    print("Плохая хэш: ", hm_bad.stats())


# Запуск
if __name__ == "__main__":
    main()
    quick_test()