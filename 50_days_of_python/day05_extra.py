# Extra Challenge: Tuple of Student Sex
# You work for a school and your boss wants to know how many
# female and male students are enrolled in the school. The school
# has saved the students in a list. Your task is to write a code that
# will count how many males and females are in the list. Here is a
# list below:
# students = ['Male', 'Female', 'female', 'male', 'male', 'male',
#  'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']
# Your code should return a list of tuples. The list above should
# return:
# [(‘Male’,7), (‘female’,6)]

students = ['Male', 'Female', 'female', 'male', 'male', 'male',
            'female', 'male', 'Female', 'Male', 'Female', 'Male', 'female']

def tuple_of_student_sex(list):
    male_count = 0
    female_count = 0
    for student in list:
        if student.lower() == "male":
            male_count += 1
            #print("male count : ", male_count)

        elif student.lower() == "female":
            female_count += 1
            #print("female count : ", female_count)

    return [("Male", male_count), ("Female", female_count)]

print(tuple_of_student_sex(students))