#data types example
x = 10
y = "hello"
z = 10.1

print(type(x), type(y), type(z))
#----------------------------------
#lists example
list_of_numbers = list(range(1, 10))
print(list_of_numbers)
list_of_numbers2 = list(range(1, 10, 2))
print(list_of_numbers2)
list_of_numbers3 = [2, 4, 6, 89]
print(list_of_numbers3)
list_of_strings = ['hi', 123]
print(list_of_strings)
list_of_combined_data = ['this', 123, 'is', 2354, 'possible']
print(list_of_combined_data)
#types attribute
print(dir(int))
print(dir(str))
print(dir(float))
print(dir(list))
#-------------------------
#usage of build-in functions
students_grades = [3.4, 5.6, 6.7]
avr_grades = sum(students_grades) / len(students_grades)
print('Student\'s grades sre: ', students_grades)
print('mean values of grades: ', avr_grades)
#------------------------------------------------------------