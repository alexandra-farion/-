from math import log2, ceil

alphabet = "abcdefghijklmnopqrstuvxyz"


def f(s):
    len_s = len(s)
    n = ceil(log2(len(s)))
    while len_s < 2 ** n:
        s = "0" + s
        len_s += 1
    for i in range(n):
        print(alphabet[i], end=" ")
    print("f")
    count = 0
    for i in range(2 ** n, 2 ** (n + 1)):
        x = bin(i)[3:]
        for j in x:
            print(j, end=" ")
        print(s[count])
        count += 1



f('00111111111')
