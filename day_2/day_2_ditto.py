# Students data

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


def calculate_grade(student, grade_1, grade_2, grade_3, grade_4):
    grade = (grade_1 + grade_2 + grade_3 + grade_4) / 4
    if grade >= 8:
        summer_status = f'Enjoy your summer {student}!'
    elif grade >= 6:
        summer_status = f'{student} has summer homework.'
    else:
        summer_status = f'{student} will attend summer school.'
    return summer_status


print(calculate_grade('Maria', 10, 8, 7, 10))
print(calculate_grade('Joseph', 6, 4, 2, 6))
print(calculate_grade('Helen', 10, 9, 5, 4))
