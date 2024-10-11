first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Генераторное выражение для первого случая
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s)

# Генераторное выражение для второго случая
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second)))

# Вывод результатов
print(list(first_result))
print(list(second_result))
