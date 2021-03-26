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
