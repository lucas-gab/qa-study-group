# Variables and Math Operations

# Declare tw variables that store numbers and print() a sum, a subtraction and division and a multiplication
# Your code below this line
A = 23
B = 10
print(A + B)
print(A - B)
print(A / B)
print(A * B)

# Data Types
# Create a String
# Create an Int
# Create a Flaot
# Print two strings being concatenated
# Print two numbers being multiplied
# Print a string being multiplied
# Your code goes below this line
Paper = "Paper"
Number = 10
Grade = 2.5
print(Paper + Paper)
print(Number * Number)
print(Paper * Number)

# List Data Type
# Make a list with 5 names
# print the second and the fifth name of your list
# Make a list with a range from 1 to 20
# Print the range list
# Your code goes below this line
My_List = ["Hugo","Leticia","Eduardo","Cameron","Lucas"]
print(My_List[1:5:3])
My_List_with_range = list(range(21))
print(My_List_with_range)

# Declare a variable my_name and assign a string to it with your name
# Write your name with funky captalization like lUcAs
# print my_name on lowercase only (use .lower())
# print my_name on uppercase only (use .upper())
# print my_name correctly captalized (use .capitalize())
# Your code goes below this line
my_name = "hUgO"
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
qa_study_group = ["Hugo","Leticia","Eduardo","Cameron"]
qa_study_group.append("Lucas")
print(qa_study_group)
qa_study_group.remove("Hugo")
print(qa_study_group)
qa_study_group.sort()
print(qa_study_group)
qa_study_group.clear()
print(qa_study_group)

# Booleans
# Print a comparison that will evaluate to FALSE
# Print a comparison that will evaluate to TRUE
# Your code goes below this line
print(20 < 2)
print(20 > 2)

# Dictionaries
# Create a dictionary that has your info
# it should have name, email, age and country
# Your code goes below this line
user = {
    "Name" : "Hugo",
    "Email" : "hugo.syrio@carta.com",
    "Age" : 32,
    "Country" : "Brazil"
    }

# Tuple
# Declare a variable and assign a Tuple to it
# Try to use any built in methods to modify it and see the results
# Your code goes below this line
TheTuple =  (25,10,15)
print(TheTuple.count(15))