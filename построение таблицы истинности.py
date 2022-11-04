def f(n, count):
    if n > count:
        for i in (0, 1):
            a.append(i)
            f(n, count + 1)


a = []
f(2, 0)
n = 2
print(a)
b = []
c = []
for i in a:
    if len(b) < n:
        b.append(i)
    else:
        c.append(b)
        b = [i]
c.append(b)
print(c)