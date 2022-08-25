# Dictionary

my_list = ["Eduardo", "Paula", "Leticia"]

coding_study_group = {
    "paticipants": {
        "names": ["Eduardo", "Hugo", "Alex"],
        "age": [31, 30, 32]
    }
}

print(coding_study_group['paticipants']['names'][1])

print(coding_study_group.get("paticipants").get('names')[1])


# Tuple

my_list = ["Eduardo", "Hugo", "Alex"]
my_tuple = ("Eduardo", "Hugo", "Alex")

my_list.append("Andrew")

print(my_list)

print(my_tuple)

# Functions

def calculate_final_grade(student_name, first_grade, second_grade, third_grade, fourth_grade):
    final_grade = (first_grade + second_grade + third_grade + fourth_grade) / 4

    print(f"{student_name}'s final grade is {final_grade}") 

calculate_final_grade("Patty", 10, 8, 9, 8)
calculate_final_grade("Eduardo", 7, 8, 10, 8)
calculate_final_grade("Gabriel", 4, 8, 7, 8)

# Conditionals

my_age = 21

if my_age < 18:
    print("Too young. Go home.")
elif my_age >= 18 and my_age < 21:
    print("You can come in with a parent.")
else:
    print('Please come in.')



