# Variables and Math Operations

# Declare tw variables that store numbers and print() a sum, a subtraction and division and a multiplication
# Your code below this line

a = 100
b = 10

print(a + b)
print(a - b)
print(a / b)
print(a * b)

# Data Types
# Create a String
message_1 = "I'm "
message_2 = "rolling with the homies"
# Create an Int
myInt = 5
# Create a Flaot
myFloat = 5.5
# Print two strings being concatenated
print(message_1 + message_2)
# Print two numbers being multiplied
print(myInt * myFloat)
# Print a string being multiplied
print(message_2 * myInt)

# List Data Type
# Make a list with 5 names
myList = ["Lucas", "Cameron", "Let", "Andrew", "Edu"]
# print the second and the fifth name of your list
print(myList[1])
print(myList[4])

# Make a list with a range from 1 to 20
myRange = [*range(1, 20)]
# Print the range list
print(myRange)

# Declare a variable my_name and assign a string to it with your name
# Write your name with funky captalization like lUcAs
myName = "cAmErOn"
# print my_name on lowercase only (use .lower())
print(myName.lower())
# print my_name on uppercase only (use .upper())
print(myName.upper())
# print my_name correctly captalized (use .capitalize())
print(myName.capitalize())

# Declare a variable named qa_study_group and assign a list to it
# The list must contain at least 4 names of people on the QA Study Group
qa_study_group = ["Cam", "Lucas", "Hugo", "Edu"]
# Add another student to the list and print the result (use .append())
qa_study_group.append("Jake")
# Remove one student from the list and print the result (use .remove())
qa_study_group.remove("Cam")
# Declare a new variable called copy_qa_study_group and assign a copy of the first list to it and print the result (use .copy())
copy_qa_study_group = qa_study_group.copy()
print(copy_qa_study_group)
# Sort the original list and print the result (use .sort())
qa_study_group.sort()
print(qa_study_group)
# Print the length of the list to see how many students are in it (use len())
print(len(qa_study_group))
# Clear the list and print out the result (use .clear())
qa_study_group.clear()
print(qa_study_group)

# Booleans
# Print a comparison that will evaluate to FALSE
print(10 == 11)
# Print a comparison that will evaluate to TRUE
print(10 == 10)

# Dictionaries
# Create a dictionary that has your info
# it should have name, email, age and country
myDict = {"Name": "Cameron", "Email": "cameron.clegg@carta.com", "Age": 31, "Country": "USA"}
print(myDict)

# Tuple
# Declare a variable and assign a Tuple to it
myTuple = ("Eggs", "Bacon", "Yogurt", "Eggs")
# Try to use any built in methods to modify it and see the results
print(myTuple.count("Eggs"))
print(myTuple.index("Bacon"))
