# Минимальный калькулятор
class Stack:
    def __init__(self): self.data = []

    def push(self, x): self.data.append(x)

    def pop(self): return self.data.pop() if self.data else None

    def peek(self): return self.data[-1] if self.data else None

    def empty(self): return not self.data


# Инфикс -> ОПН
def to_rpn(expr):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    out, s = [], Stack()

    i = 0
    while i < len(expr):
        if expr[i].isdigit():
            j = i
            while j < len(expr) and expr[j].isdigit():
                j += 1
            out.append(expr[i:j])
            i = j
        elif expr[i] in '+-*/^':
            while (not s.empty() and s.peek() in prec and
                   prec[s.peek()] >= prec[expr[i]]):
                out.append(s.pop())
            s.push(expr[i])
            i += 1
        elif expr[i] == '(':
            s.push(expr[i])
            i += 1
        elif expr[i] == ')':
            while not s.empty() and s.peek() != '(':
                out.append(s.pop())
            s.pop()  # удаляем '('
            i += 1
        else:
            i += 1

    while not s.empty():
        out.append(s.pop())

    return out


# Вычисление ОПН
def calc_rpn(rpn):
    s = Stack()
    for t in rpn:
        if t.isdigit():
            s.push(int(t))
        else:
            b, a = s.pop(), s.pop()
            if t == '+':
                s.push(a + b)
            elif t == '-':
                s.push(a - b)
            elif t == '*':
                s.push(a * b)
            elif t == '/':
                s.push(a / b)
            elif t == '^':
                s.push(a ** b)
    return s.pop()


# Все в одной функции
def calculate(expr):
    prec = {'+': 1, '-': 1, '*': 2, '/': 2}
    ops = {'+': lambda a, b: a + b, '-': lambda a, b: a - b,
           '*': lambda a, b: a * b, '/': lambda a, b: a / b}

    # Простой парсер
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isdigit():
            j = i
            while j < len(expr) and expr[j].isdigit():
                j += 1
            tokens.append(int(expr[i:j]))
            i = j
        elif expr[i] in '+-*/':
            tokens.append(expr[i])
            i += 1
        else:
            i += 1

    # Конвертация
    out, stack = [], []
    for t in tokens:
        if isinstance(t, int):
            out.append(t)
        else:
            while stack and stack[-1] in prec and prec[stack[-1]] >= prec[t]:
                out.append(stack.pop())
            stack.append(t)

    while stack:
        out.append(stack.pop())

    # Вычисление
    s = []
    for t in out:
        if isinstance(t, int):
            s.append(t)
        else:
            b, a = s.pop(), s.pop()
            s.append(ops[t](a, b))

    return s[0]


# Демо
print("=== КАЛЬКУЛЯТОР ===")
expr = "3+4*2"
rpn = to_rpn(expr)
result = calc_rpn(rpn)
print(f"{expr} -> ОПН: {' '.join(rpn)} = {result}")
print(f"calculate('{expr}') = {calculate(expr)}")

# Еще примеры
tests = ["3+4", "2*3+4", "2+3*4", "10-2*3"]
for t in tests:
    print(f"{t} = {calculate(t)}")