# new_dict = {new_key : new_value for (key, value) in dict.items()}
# new_dict = {new_key : new_value for (key, value) in dict.items() if test}
import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

students_scores = {student : random.randint(1, 100) for student in names}
print(students_scores)  # {'Alex': 10, 'Beth': 5, 'Caroline': 44, 'Dave': 5, 'Eleanor': 78, 'Freddie': 97}

passed_students = {student : score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)  # {'Eleanor': 78, 'Freddie': 97}