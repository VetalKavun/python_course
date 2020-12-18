myfile = open("fruits.txt")
print(myfile.read())
myfile.close()

with open("/home/vitaliy/git/python_course/section_2/fruits2.txt") as myfile:
    content = myfile.read()

with open("numbers.txt", "w") as numbers:
    numbers.write("one")

