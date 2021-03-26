#1
for i in range(150):
    print(i)

#2
for num in range(5,1000):
    if num % 5 == 0:
        print(num)

#3
for num in range(1,100):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)

#4
for j in range(2018, 1, -4):
    print(j)

#5

lowNum=3
highNum=100
mult=2
for num in range (lowNum,highNum):
    if num % mult == 0:
        print(num)