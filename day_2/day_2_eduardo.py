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

# Now we need to calculate the final grade of each student (sum of all grades divided by 4)
# We also need to evaluate if the student is going to have summer vacations or not
# If the student has a grade greater than or equal 8, then they are free to enjoy their summer vacations
# If the student has a grade smaller than 8, but higher or equal to 6, then they are getting some summer homework
# If the student has a grade smaller than 6, then they will stay in school during summer
# Declare a function that calculates the final grade of each student
# The same function will have to print a message to the terminal stating if the student will have summer vacations,
# will have summer homework or will have to stay in school during summer
# Use functions and conditionals to achieve this
# Your code goes below this line

def final_grade_1(student_1, grade_1, grade_2, grade_3, grade_4):
    final_grade_result_1 = (grade_1 + grade_2 + grade_3 + grade_4)/4
    if final_grade_result_1 >= 8:
        print(f"Final grade: {final_grade_result_1}. Enjoy your summer vacation, {student_1}!")
    elif final_grade_result_1 > 6:
        print(f"Final grade: {final_grade_result_1}.Here's your summer homework, {student_1}")
    else:
        print(f"Final grade: {final_grade_result_1}. Too bad, guess you are stuck at school, {student_1}")

final_grade_1(student_1, student_1_first_grade, student_1_second_grade, student_1_third_grade, student_1_fourth_grade)

def final_grade_2(student_2, grade_1, grade_2, grade_3, grade_4):
    final_grade_result_2 = (grade_1 + grade_2 + grade_3 + grade_4)/4
    if final_grade_result_2 >= 8:
        print(f"Final grade: {final_grade_result_2}. Enjoy your summer vacation, {student_2}!")
    elif final_grade_result_2 > 6:
        print(f"Final grade: {final_grade_result_2}. Here's your summer homework, {student_2}")
    else:
        print(f"Final grade: {final_grade_result_2}. Too bad, guess you are stuck at school, {student_2}")

final_grade_2(student_2, student_2_first_grade, student_2_second_grade, student_2_third_grade, student_2_fourth_grade)

def final_grade_3(student_3, grade_1, grade_2, grade_3, grade_4):
    final_grade_result_3= (grade_1 + grade_2 + grade_3 + grade_4)/4
    if final_grade_result_3 >= 8:
        print(f"Final grade: {final_grade_result_3}. Enjoy your summer vacation, {student_3}!")
    elif final_grade_result_3 > 6:
        print(f"Final grade: {final_grade_result_3}. Here's your summer homework, {student_3}")
    else:
        print(f"Too bad, guess you are stuck at school, {student_3}")

final_grade_3(student_3, student_3_first_grade, student_3_second_grade, student_3_third_grade, student_3_fourth_grade)


