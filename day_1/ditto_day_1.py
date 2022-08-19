# Variables and Math Operations

# Declare tw variables that store numbers and print() a sum, a subtraction and division and a multiplication
# Your code below this line
int_1 = 1
int_2 = 2
print(int_1 + int_2)
print(int_1 - int_2)
print(int_1 / int_2)
print(int_1 * int_2)


# Data Types
# Create a String
# Create an Int
# Create a Float
# Print two strings being concatenated
# Print two numbers being multiplied
# Print a string being multiplied
# Your code goes below this line
my_str = 'Words in a string'
my_int = 3
my_float = 4.5
my_str_2 = ' and other string'
print(my_str + my_str_2)
print(my_int * my_float)
print(my_str * my_int)


# List Data Type
# Make a list with 5 names
# print the second and the fifth name of your list
# Make a list with a range from 1 to 20
# Print the range list
# Your code goes below this line
my_list = ['Jake', 'Brian', 'Ben', 'Josh', 'Jacob']
print(my_list[1:5:3])
my_list_2 = list(range(21))
print(my_list_2)


# Declare a variable my_name and assign a string to it with your name
# Write your name with funky captalization like lUcAs
# print my_name on lowercase only (use .lower())
# print my_name on uppercase only (use .upper())
# print my_name correctly captalized (use .capitalize())
# Your code goes below this line
my_name = 'dIttO'
print(my_name.lower())
print(my_name.upper())
print(my_name.capitalize())


# Declare a variable named qa_study_group and assign a list to it
# The list must contain at least 4 names of people on the QA Study Group
# Add another student to the list and print the result (use .append())
# Remove one student from the list and print the result (use .remove())
# Declare a new variable called copy_qa_study_group and assign a copy of the first list to it and print the result (use .copy())
# Sort the original list and print the result (use .sort())
# Print the length of the list to see how many students are in it (use len())
# Clear the list and print out the result (use .clear())
# Your code goes below this line
qa_study_group = ['Ditto', 'Lucas', 'Cameron', 'Alex']
qa_study_group.append('Sezim')
qa_study_group.remove('Ditto')
qa_study_group.sort()
print(len(qa_study_group))
qa_study_group.clear()


# Booleans
# Print a comparison that will evaluate to FALSE
# Print a comparison that will evaluate to TRUE
# Your code goes below this line
print(1 < 0)
print(1 > 0)


# Dictionaries
# Create a dictionary that has your info
# it should have name, email, age and country
# Your code goes below this line
my_dict = {
    'name': 'A. Ditto',
    'email': 'andrew.ditto@carta.com',
    'age': 33,
    'country': 'USA'
}


# Tuple
# Declare a variable and assign a Tuple to it
# Try to use any built in methods to modify it and see the results
# Your code goes below this line
my_tuple = ('a', 1)
print(my_tuple.count('a'))
