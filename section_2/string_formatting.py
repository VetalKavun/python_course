def greeting(name):
    return "Hello, %s" % name


def greeting2(name):
    return f"Hello, {name}"


name = input("Enter your name: ")
print(greeting2(name))