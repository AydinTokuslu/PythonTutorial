# Write a function called student_marks that records marks
# achieved by students in a test. The function should ask the user
# to input the name of the student and then ask the user to input
# the marks achieved by the student. The information should be
# stored in a dictionary. The name is the key and the marks is the
# value. When the user enters done, the function should return a
# dictionary of names and values entered.

def student_marks():
    info = {}
    while True:
        name=input("please enter your name or done: ")
        if name == "done":
            break
        marks=int(input("please enter your marks: "))
        #print(info.get(marks,0))
        info[name]=marks
        #info[name]=int(info.get(marks)) + marks
        info[name]=int(info[name]) + marks
    return info


print(student_marks())