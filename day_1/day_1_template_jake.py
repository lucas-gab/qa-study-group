# Variables and Math Operations

# Declare tw variables that store numbers and print() a sum, a subtraction and division and a multiplication
# Your code below this line

holderOne = 2
holderTwo = 5

print(holderOne + holderTwo)
print(holderOne - holderTwo)
print(holderOne * holderTwo)
print(holderOne / holderTwo)

# Data Types
# Create a String
# Create an Int
# Create a Flaot
# Print two strings being concatenated
# Print two numbers being multiplied
# Print a string being multiplied
# Your code goes below this line
inputString = "Hello my name is Jake"
inputInt = 12
inputFloat = 1.2

inputStringOne = "Hello my name is"
inputStringTwo = "Jake Saylor"
print(f"{inputStringOne} {inputStringTwo}")

inputIntOne = 3
inputIntTwo = 2
print(inputIntOne * inputIntTwo)

inputStringMult = "This is Jake" #?????

# List Data Type
# Make a list with 5 names
# print the second and the fifth name of your list
# Make a list with a range from 1 to 20
# Print the range list
# Your code goes below this line
inputList = ["Jake", "Lucas", "Matt", "Vini", "Alex"]
print(inputList[1])
print(inputList[4])

inputListNum = list(range(1,21))
print(inputListNum)


# Declare a variable my_name and assign a string to it with your name
# Write your name with funky captalization like lUcAs
# print my_name on lowercase only (use .lower())
# print my_name on uppercase only (use .upper())
# print my_name correctly captalized (use .capitalize())
# Your code goes below this line

my_name = "JAkE SAyLor"
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

qa_study_group = ["Jake", "Matt", "Vini", "Lucas"]
qa_study_group.append("Alex")
print(qa_study_group)
qa_study_group.remove("Jake")
print(qa_study_group)
copy_qa_study_group = qa_study_group.copy()
qa_study_group.sort()
print(qa_study_group)
print(len(qa_study_group))
print(qa_study_group.clear())


# Booleans
# Print a comparison that will evaluate to FALSE
# Print a comparison that will evaluate to TRUE
# Your code goes below this line
print(1 == 2)
print(1 == 1)


# Dictionaries
# Create a dictionary that has your info
# it should have name, email, age and country
# Your code goes below this line
inputDic = {["Jake", "jakesaylor@test.com", 26, "USA"]}


# Tuple
# Declare a variable and assign a Tuple to it
# Try to use any built in methods to modify it and see the results
# Your code goes below this line
inputTuple = ("Jake", "Lucas", "Vini")
inputTuple