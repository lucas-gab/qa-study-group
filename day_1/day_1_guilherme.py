# Variables and Math Operations

# Declare tw variables that store numbers and print() a sum, a subtraction and division and a multiplication
# Your code below this line
x = 10
y = 20
print(x+y)
print(x-y)
print(x/y)
print(x*y)

# Data Types
# Create a String
# Create an Int
# Create a Flaot
# Print two strings being concatenated
# Print two numbers being multiplied
# Print a string being multiplied
# Your code goes below this line
str = "text "
str2 = "concatenated"
int = 10
int2 = 2
float = 5.5
print(str+str2)
print(int*int2)
print(str2*2)

# List Data Type
# Make a list with 5 names
# print the second and the fifth name of your list
# Make a list with a range from 1 to 20
# Print the range list
# Your code goes below this line
name_list = ["alex", 'john', "mary", 'bob', 'tom']
print(name_list[1],name_list[4])
list_from_one_to_twent = list(range(1, 11))
print(list_from_one_to_twent)


# Declare a variable my_name and assign a string to it with your name
# Write your name with funky captalization like lUcAs
# print my_name on lowercase only (use .lower())
# print my_name on uppercase only (use .upper())
# print my_name correctly captalized (use .capitalize())
# Your code goes below this line
my_name = "gUiLhErMe"

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
qa_study_group = ["lucas", "alex", "cameron", "hugo"]
print(qa_study_group)
qa_study_group.append("eduardo")
print(qa_study_group)
qa_study_group.remove("alex")
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
int = 1
int2 = 2
int3 = 2

print(int == int2)
print(int3 == int2)

# Dictionaries
# Create a dictionary that has your info
# it should have name, email, age and country
# Your code goes below this line
myDictionary = {'name': 'guilherme', 'email': 'guilherme@email.com', 'age': 35, 'country': 'brazil'}
print(myDictionary)

# Tuple
# Declare a variable and assign a Tuple to it
# Try to use any built in methods to modify it and see the results
# Your code goes below this line
myTuple = ()

