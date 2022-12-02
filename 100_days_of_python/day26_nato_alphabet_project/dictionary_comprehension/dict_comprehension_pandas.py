import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score":[56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
# student  score
# 0  Angela     56
# 1   James     76
# 2    Lily     98

for (index, row) in student_data_frame.iterrows():
    #print(row.student)  # Angela, James, Lily
    #print(row.score)  # 56, 76, 98
    if row.student == "Angela":
        print(row.score)  # 56