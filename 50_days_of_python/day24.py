# Create a function called average_calories that calculates the
# average calories intake of a user. The function should ask the user
# to input their calories intake for any number of days and once they
# hit ‘done’ it should calculate and return the average intake.

def average_calories():
    scores=[]
    while True:
        score=input("please enter a score or done when quit: ")
        if score=="done":
            break
        scores.append(int(score))
    return f"mean of score is {sum(scores)/len(scores)}"

print(average_calories())