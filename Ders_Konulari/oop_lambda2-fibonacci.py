
# fibonacciye göre bulalım, 0,1,2,3,5,8,13 ....

def fibonacci(length):
    resultList=list() # yada []
    if length <= 0:
        return resultList
    resultList.append(0)
    if length == 1:
        return resultList
    resultList.append(1)
    if length == 2:
        return resultList
    resultList.append(2) # listemizi 0, 1, 2 olarak oluşturduk.

    for index in range(2, length+1):
        resultList.append(resultList[-2] + resultList[-1])

    return resultList
print(fibonacci(15))
# [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
print(sum(fibonacci(15))) # 4179