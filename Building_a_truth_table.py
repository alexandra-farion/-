def f(n, a):
    for i in range(n):
        print(a[i], end=" ")
    print("f")
    for i in range(2 ** n, 2 ** (n + 1)):
        x = bin(i)[3:]
        for j in x:
            print(j, end=" ")
        print()


a = ["x", "y", "z"]
f(3, a)
