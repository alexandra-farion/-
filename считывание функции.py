# Обозначения

# Логические операции:
# Отрицание  ~
# Конъюнкция ^
# Дизъюнкция v
# Импликация ->
# Эквиваленция <->
# Неэквивалентность -v
# Символ Шеффера |
# Стрелка Пирса v|

# Переменные записываются латинскими буквами в верхнем регистре. Букву v использовать нельзя!

print("Введите булеву функцию. Каждый знак, переменная, значение пишите через пробел")
s = input()
f = s.split(" ")
variables = s.split(" ")
print(f)
removed_chars = ['~', '^', 'v', '-', '<', '>', '|', ' ']

chars = set(removed_chars)
# res = ''.join(filter(lambda x: x not in chars, s))
res = list(set(filter(lambda x: x not in chars, s)))
print(res)


# number_of_variables = 3
# number_of_options = 2 ** number_of_variables