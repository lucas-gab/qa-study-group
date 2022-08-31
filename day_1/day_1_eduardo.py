# Variables and Math Operations

# Declare tw variables that store numbers and print() a sum, a subtraction and division and a multiplication
# Your code below this line
x = 10
y = 5

print(x+y)
print(x-y)
print(x/y)
print(x*y)

# Data Types
# Create a String
# Create an Int
# Create a Float
# Print two strings being concatenated
# Print two numbers being multiplied
# Print a string being multiplied
# Your code goes below this line
test = "test"
int = 100
float = 5.5
a = "My "
b = "name"
print(a + b)
print(x*y)
print(x*a)

# List Data Type
# Make a list with 5 names
# print the second and the fifth name of your list
# Make a list with a range from 1 to 20
# Print the range list
# Your code goes below this line
list_name = ["Eduardo", "Marina", "Malu", "Maria Lucia", "Maluela"]
print(list_name[1], list_name[4])
range_list = list(range(1, 21))
print(range_list)

# Declare a variable my_name and assign a string to it with your name
# Write your name with funky captalization like lUcAs
# print my_name on lowercase only (use .lower())
# print my_name on uppercase only (use .upper())
# print my_name correctly captalized (use .capitalize())
# Your code goes below this line
my_name = "eDuArDo"
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
qa_study_group = ["Lucas", "Eduardo", "Vini", "Leticia"]
qa_study_group.append("Hugo")
print(qa_study_group)
qa_study_group.remove("Eduardo")
print(qa_study_group)

copy_qa_study_group = qa_study_group.copy()
print(copy_qa_study_group)

qa_study_group.sort()
print(qa_study_group)

print(len(qa_study_group))

qa_study_group.clear()
print(qa_study_group)

# Booleans
# Print a comparison that will evaluate to FALSE
# Print a comparison that will evaluate to TRUE
# Your code goes below this line
print(5==4)
print(5==5)

# Dictionaries
# Create a dictionary that has your info
# it should have name, email, age and country
# Your code goes below this line
my_dictionary = {"Name": "Eduardo", "email": "eduardo.bacil@carta.com", "Age": 29, "Country": "Brazil"}
print(my_dictionary.values())
print(my_dictionary.keys())

# Tuple
# Declare a variable and assign a Tuple to it
# Try to use any built in methods to modify it and see the results
# Your code goes below this line

my_tupple = ("I", "Do not", "understand", "tupples")
print(my_tupple[0], my_tupple[2])

print(len(my_tupple))

my_tupple.sort()
print(my_tupple)