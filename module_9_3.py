first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторная сборка для первой переменной
first_result = (abs(len(f) - len(s)) for f, s in zip(first, second) if len(f) != len(s))

# Генераторная сборка для второй переменной
second_result = (len(first[i]) != len(second[i]) for i in range(len(first)))

# Пример
print(list(first_result))   # [1, 2]
print(list(second_result))  # [False, False, True]
