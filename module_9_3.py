first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# Операция 1: Генераторная сборка для вычисления разницы длин строк из списков first и second
first_result = ((len(a) - len(b)) for a, b in zip(first, second) if len(a) != len(b))

# Операция 2: Генераторная сборка для сравнения длин строк в одинаковых позициях из списков first и second
second_result = ((len(first[i]) == len(second[i])) for i in range(len(first)))

print(list(first_result))
print(list(second_result))
