def greeting(name, age):
    return "Hello, %s! You told, you are: %d" % (name, age)


def greeting2(name, age):
    return f"Hello, {name}! You told, you are: {age}"


name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(greeting2(name, age))
print(greeting(name, age))
