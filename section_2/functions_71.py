def add(a, b):
    return a + b


def add2(a, b=3):
    return a + b


print(add(2, 4))
print(add(b=5, a=2))
print(add2(3))