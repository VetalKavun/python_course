def add(a, b):
    return a + b


def add2(a, b=3):
    return a + b


def str_printer(*args):
    print(args)


print(add(2, 4))
print(add(b=5, a=2))
print(add2(3))
print(str_printer('q', 'w', 4, 5))
