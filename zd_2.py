import time


class StaticArray:
    def __init__(self, cap=100):
        self.cap, self.data, self.size = cap, [None] * cap, 0

    def push_back(self, v):  # O(1)
        if self.size >= self.cap: raise IndexError("Full")
        self.data[self.size], self.size = v, self.size + 1

    def __str__(self): return f"[{', '.join(str(self.data[i]) for i in range(self.size))}]"


class DynamicArray:
    def __init__(self, init_cap=10):
        self.cap, self.data, self.size = init_cap, [None] * init_cap, 0

    def _resize(self, new_cap):  # O(n) - копирование всех элементов
        new_data = [None] * new_cap
        for i in range(self.size):
            new_data[i] = self.data[i]
        self.data, self.cap = new_data, new_cap

    def push_back(self, v):  # Амортизированная O(1)
        if self.size >= self.cap:
            self._resize(self.cap * 2)  # Стратегия ×2
        self.data[self.size], self.size = v, self.size + 1

    def __str__(self):
        return f"[{', '.join(str(self.data[i]) for i in range(self.size))}]"


def test_performance():
    print("=== Сравнение производительности ===")
    n = 100000

    # Тест статического массива
    print(f"\n1. Статический массив (вместимость: {n})")
    start = time.time()
    static_arr = StaticArray(n)
    for i in range(n):
        static_arr.push_back(i)
    static_time = time.time() - start
    print(f"   Время: {static_time:.4f} сек")
    print(f"   Размер: {static_arr.size}, Вместимость: {static_arr.cap}")

    # Тест динамического массива
    print(f"\n2. Динамический массив (начальная вместимость: 10)")
    start = time.time()
    dynamic_arr = DynamicArray(10)
    for i in range(n):
        dynamic_arr.push_back(i)
    dynamic_time = time.time() - start
    print(f"   Время: {dynamic_time:.4f} сек")
    print(f"   Размер: {dynamic_arr.size}, Вместимость: {dynamic_arr.cap}")

    # Сравнение
    print(f"\n3. Сравнение:")
    print(f"   Разница во времени: {dynamic_time / static_time:.2f}x")
    print(f"   Статический: {static_time:.4f} сек")
    print(f"   Динамический: {dynamic_time:.4f} сек")

    # Анализ расширений
    print(f"\n4. Анализ расширений динамического массива:")
    print(f"   Начальная вместимость: 10")
    print(f"   Финальная вместимость: {dynamic_arr.cap}")
    print(f"   Коэффициент расширения: {dynamic_arr.cap / 10}")

    # Показываем логи расширения
    print(f"\n5. Логика расширения (стратегия ×2):")
    print(f"   10 → 20 → 40 → 80 → 160 → 320 → ...")
    print(f"   Последнее расширение до: {dynamic_arr.cap}")


def demonstrate_dynamic():
    print("\n=== Демонстрация динамического массива ===")
    arr = DynamicArray(3)

    print("Начальный массив (емкость=3):")
    print(f"  Размер: {arr.size}, Емкость: {arr.cap}")

    # Добавляем элементы, наблюдая за расширением
    for i in range(1, 10):
        arr.push_back(i * 10)
        print(f"  Добавили {i * 10}: размер={arr.size}, емкость={arr.cap}")

    print(f"\nФинальный массив:")
    print(f"  Размер: {arr.size}, Емкость: {arr.cap}")
    print(f"  Данные: {arr}")


def complexity_explanation():
    print("\n=== Объяснение сложности ===")
    print("\n1. Статический массив (push_back):")
    print("   - Всегда O(1)")
    print("   - Просто запись в память")

    print("\n2. Динамический массив (push_back):")
    print("   - Амортизированная O(1)")
    print("   - Обычно O(1)")
    print("   - При расширении: O(n) (копирование)")
    print("   - Но расширения редки (×2 стратегия)")

    print("\n3. Почему динамический медленнее?")
    print("   - Дополнительные проверки на расширение")
    print("   - Копирование данных при resize()")
    print("   - Но удобен - не нужно знать размер заранее")


if __name__ == "__main__":
    # Запускаем демонстрацию
    demonstrate_dynamic()

    # Запускаем тест производительности
    test_performance()

    # Показываем объяснение
    complexity_explanation()

    # Пример использования
    print("\n=== Пример быстрого использования ===")
    dyn = DynamicArray(2)
    for i in range(5):
        dyn.push_back(i)
        print(f"Добавил {i}: размер={dyn.size}, емкость={dyn.cap}")