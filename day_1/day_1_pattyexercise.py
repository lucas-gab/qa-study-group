# Variables and Math Operations

# Declare two variables that store numbers and print() a sum, a subtraction and division and a multiplication
# Your code below this line

one = 1
eight = 8

print (one + eight)
print (eight - one)
print (one / eight)
print (one * eight)

# Data Types
# Create a String
# Create an Int
# Create a Float
# Print two strings being concatenated
# Print two numbers being multiplied
# Print a string being multiplied
# Your code goes below this line

name = 'Patricia'
lastname = 'Souza'
age = 31
weight = 81.5

print (name +' '+ lastname)
print (age*weight)
print (name*eight)

# List Data Type
# Make a list with 5 names
# print the second and the fifth name of your list
# Make a list with a range from 1 to 20
# Print the range list
# Your code goes below this line

apr18_cohort = ['Mario', 'Pablo', 'Paty Escobar','Patty Souza', 'Pedro']
print (apr18_cohort[1],apr18_cohort[4])

list_1to20 = list(range(1, 21))
print(list_1to20)

# Declare a variable my_name and assign a string to it with your name
# Write your name with funky captalization like lUcAs
# print my_name on lowercase only (use .lower())
# print my_name on uppercase only (use .upper())
# print my_name correctly captalized (use .capitalize())
# Your code goes below this line

my_name = 'PaTriCIa'
print (my_name.lower()) #or print(my_name.casefold())
print (my_name.upper())
print (my_name.capitalize())

# Declare a variable named qa_study_group and assign a list to it
# The list must contain at least 4 names of people on the QA Study Group
# Add another student to the list and print the result (use .append())
# Remove one student from the list and print the result (use .remove())
# Declare a new variable called copy_qa_study_group and assign a copy of the first list to it and print the result (use .copy())
# Sort the original list and print the result (use .sort())
# Print the length of the list to see how many students are in it (use len())
# Clear the list and print out the result (use .clear())
# Your code goes below this line

qa_study_group = ['Alex','Andrew','Christian','Eduardo','Barella','Jake','Leticia','Louise']
qa_study_group.append('Hugo')
print(qa_study_group)
qa_study_group.remove('Leticia')
print(qa_study_group)

copy_qa_study_group = qa_study_group.copy()
qa_study_group.sort()
print(qa_study_group)
print(len(qa_study_group))

qa_study_group.clear()
print(qa_study_group)



# Booleans
# Print a comparison that will evaluate to FALSE
# Print a comparison that will evaluate to TRUE
# Your code goes below this line

print (10 > 20)
print (10 < 20)

# Dictionaries
# Create a dictionary that has your info
# it should have name, email, age and country
# Your code goes below this line

patty_info = {'Name': my_name, 'E-mail': 'patricia.souza@carta.com', 'Age': age, 'Country': 'Brazil'}

# Tuple
# Declare a variable and assign a Tuple to it
# Try to use any built in methods to modify it and see the results
# Your code goes below this line

rio_temperatures = (25.0, 27.3, 31.0)
rio_temperatures.append(50)

print (rio_temperatures)
