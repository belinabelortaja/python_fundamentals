def insertion_sort(myList):  
        for i in range(len(myList)):  
            first_ind = myList[i]  
            j = i - 1  
            while j >= 0 and first_ind < myList[j]:  
                myList[j + 1] = myList[j]  
                j -= 1  
            myList[j + 1] = first_ind  
        return myList
newList = [10, 5, 13, 8, 2]  
print(insertion_sort(newList))