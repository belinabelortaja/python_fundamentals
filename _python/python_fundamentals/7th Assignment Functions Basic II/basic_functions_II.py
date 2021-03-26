#1
def countdown(myList):
    myNexList = []
    for x in range(myList, 0, -1):
        myNexList.append(x)
    return myNexList
print(countdown(7))


#2
def prRet(a,b):
    print(a)
    return b
print(prRet(1,4))

#3
def firstPlusLength(myList):
    sum=0
    for sum in range (0,len(myList),1):
        sum = myList[0] + len(myList)
        return sum
newList = [1,4,6,3,6,4]
print(firstPlusLength(newList))

#4
def greaterThanSecond(my1List):
        nextList= []
        for x in my1List:
            if x > my1List[1]:
                nextList.append(x)
                print(nextList)
                print(len(nextList))
        else:
            print(False)              
new1List = [6,4,32,8,1]
print(greaterThanSecond(new1List))

#5 ?????
def lengthAndValue(length,value):
    myNexList = []
    for x in range(length):
        myNexList.append(x)
    for y in range(value):
        value = y
    return myNexList
print(lengthAndValue(5,2))






