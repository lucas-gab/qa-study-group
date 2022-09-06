# Students data

from concurrent.futures import thread
import threading
from typing import Final


student_1 = "Maria"
student_1_first_grade = 10
student_1_second_grade = 8
student_1_third_grade = 7
student_1_fourth_grade = 10

student_2 = "Joseph"
student_2_first_grade = 6
student_2_second_grade = 4
student_2_third_grade = 2
student_2_fourth_grade = 6

student_3 = "Helen"
student_3_first_grade = 10
student_3_second_grade = 9
student_3_third_grade = 5
student_3_fourth_grade = 4

# Now we need to calculate the final grade of each student (sum of all grades diveded by 4)
# We also need to evaluate if the student is going to have summer vacations or not
# If the student has a grade greater than or equal 8, then they are free to enjoy their summer vacations
# If the student has a grade smaller than 8, but higher or equal to 6, then they are getting some summer homework
# If the student has a grade smaller than 6, then they will stay in school during summer



# Declare a function that calculates the final grade of each student
# The same function will have to print a message to the terminal stating if the student will have summer vacations, 
# will have summer homework or will have to stay in school during summer
# Use functions and conditionals to achieve this
# Your code goes below this line
def Final_grade_calculator(student_name, first_grade, second_grade, third_grade, fourth_grade):
    final_grade = (first_grade + second_grade + third_grade + fourth_grade)/4
    print(f"{student_name}'s final grade is {final_grade}")
    if final_grade >= 8:
        print(f"{student_name} is free to enjoy summer vacations")
    elif final_grade >= 6 and final_grade < 8:
        print(f"{student_name} is getting some summer homework")
    else:
        print(f"{student_name} will stay in school during summer")

Final_grade_calculator(student_1,student_1_first_grade,student_1_second_grade,student_1_third_grade,student_1_fourth_grade)
Final_grade_calculator(student_2,student_2_first_grade,student_2_second_grade,student_2_third_grade,student_2_fourth_grade)
Final_grade_calculator(student_3,student_3_first_grade,student_3_second_grade,student_3_third_grade,student_3_fourth_grade)