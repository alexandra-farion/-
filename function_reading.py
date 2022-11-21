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

def negation(x):
    return not x


def conjunction(x, y):
    return x and y


def disjunction(x, y):
    return x or y


def implication(x, y):
    return x <= y


def equivalence(x, y):
    return x == y


def nonequivalence(x, y):
    return x != y


def schaeffer_symbol(x, y):
    return not (x and y)


def pierce_arrow(x, y):
    return not (x or y)


print("Введите булеву функцию. Каждый знак, переменная, значение пишите через пробел")
s = input()
f = s.split(" ")
variables = s.split(" ")
print(f)
removed_chars = ['~', '^', 'v', '<->', '->', '|', '-v', 'v|']
flag = False
for i in f:
    print(i, end=" ")
