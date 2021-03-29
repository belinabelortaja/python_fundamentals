def selectionSort( myList ):
    for i in range( len(myList) - 1 ): 
        minValueIndex = i
        for j in range( i + 1, len(myList) ):
            if myList[j] < myList[minValueIndex] :
                minValueIndex = j
        if minValueIndex != i :
            temp = myList[i]
            myList[i] = myList[minValueIndex]
            myList[minValueIndex] = temp
    return myList
newList = [21,6,9,33,3]
print(selectionSort(newList))