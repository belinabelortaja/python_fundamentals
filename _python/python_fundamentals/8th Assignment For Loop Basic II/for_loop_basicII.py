# 1

def biggieSize(myList):
    for i in myList:
        i < myList.length
        i += 1
    if myList[i] > 0:
        myList[i] = "big"
    return myList


newList = [10, -3, 5, -7, 8, 6]
print(biggieSize(newList))

# 2


def countPositives(myList):
    count = 0
    for x in range(0, len(myList), 1):
        if myList[x] > 0:
            count += 1
        myList[len(myList)-1] = count
        print(myList)


newList = [-3, -2, 5, 7]
print(countPositives(newList))

# 3


def sum_of_list(myList):
    sum = 0
    for i in myList:
        sum = sum + i
    return sum


my_list = [1, 8, 5, 2, 4]
print(sum_of_list(my_list))

# 4


def average(myList):
    sum = 0
    for i in myList:
        sum = sum + i

    avg = sum / len(myList)
    return avg


newList = [4, 6, 32, 5]

print(average(newList))

# 5


def length(myList):

    return len(myList)


newList = [4, 6, 32, 5, 8]

print(length(newList))

# 6


def min(myList):
    num = myList[0]
    for i in myList:
        if num > i:
            num = i
    return num


newList = (-6, 2, 3, -10, 5, 6)
print(min(newList))

# 7


def max(myList):
    num = myList[0]
    for i in myList:
        if num < i:
            num = i
    return num


newList = (1, 2, 3, 10, 5, 6)
print(max(newList))

# 8


def sumList(myList):
    sum = 0
    for i in myList:
        sum = sum + i
    return sum


def average1(myList):
    sum = 0
    for i in myList:
        sum = sum + i
    avg = sum / len(myList)
    return avg


def length1(myList):

    return len(myList)


def min1(myList):
    num = myList[0]
    for i in myList:
        if num > i:
            num = i
    return num


def max1(myList):
    num = myList[0]
    for i in myList:
        if num < i:
            num = i
    return num


newList = (1, 2, 3, 10, 5, 6)
print(sumList(newList), average1(newList), length1(
    newList), min1(newList), max1(newList))

# 9


def reverse(myList):
    num1 = 0
    num2 = len(myList)-1
    while num1 < num2:
        temp = myList[num1]
        myList[num1] = myList[num2]
        myList[num2] = temp
        num1 += 1
        num2 -= 1
    return myList


newList = [2, 8, 3, 6, 5]
print(reverse(newList))
