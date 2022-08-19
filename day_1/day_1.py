# Variables and Math Operations

# Declare tw variables that store numbers and print() a sum, a subtraction and division and a multiplication

a = 20
b = 5

print(a + b)
print(a - b)
print(a / b)
print(a * b)

# Data Types

number = 10000  # Int
sentense = "I want to type a sentense"  # String
floatNumber = 10.4  # Float

first_sentence = "All you need is "
second_sentence = "a cheeseburger"
third_sentence = ", love"
fourth_sentence = " and a lot of money"
number_as_string = '10000'
# str() - turns a data type into a String data type
# int() - turns a data type into a Int Number data type

print(first_sentence + str(number))
print(int(number_as_string) * 2)

# List Data Type

list_names = ["Hugo", "Leticia", "Vini", "Andrew", "Imtiaj"]

mixed_list = ['Lucas', 31]

list_within_list = [['Lucas', 31], ['Paula', 28], ['John', 22]]

print(list_names[0])

print(list_within_list[0][0])

# Lists are group of data stored together by the use of [ ]
# We can access the items on the list by using the index selector list_name[0]
# Always remember that Python is 0 indexed, therefore we start counting on 0, not 1

list_from_one_to_ten = list(range(1, 11))

print(list_from_one_to_ten)

# list() is used to create a list type of data
# range(0, 11) creates a list of numbers starting at 1 and ending, but not including 11

# Methods for Strings

my_name = 'lUcAs'

my_age = 31

print(my_name.lower())

print(my_name.upper())

print(my_name.capitalize())

print(len(my_name))

print(len(list_names))

print(f'My name is {my_name} and I am {my_age}')

# Methods for Lists

list_names = ["Hugo", "Leticia", "Vini", "Andrew"]

print(len(list_names))

list_names.append("Eduardo")

print(len(list_names))

print(list_names)

list_names.remove("Hugo")

print(list_names)

qa_study_group = list_names.copy()

list_names.clear()

print(list_names)

# BOOLEANS

my_boolean = (10 == 10)

print(my_boolean)

measurements = [9.1, 8.8, 7.5, 5.6, 7.9, 3.1, 9.8]
print(measurements)
print(measurements[1:])
print(measurements[:-1])
print(measurements[-3:])


Insane = 'Crazzzzzy'
print(Insane)
print(Insane[1])
print(Insane[:3])
print(Insane[:-3])


print('Lukas' .replace('k', 'c'))


The_word = 'Crazzzzzy'
Letters_list = list(The_word)
print(Letters_list)

Letters_list = ['C', 'r', 'a', 'z', 'z', 'z', 'z', 'z', 'y']
The_word = str.join('', Letters_list)
print(The_word)
