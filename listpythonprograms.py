# Python program to find smallest number in a list

numberlist = [12, 0, 89, -12, 67, 90, 0]
numberlist.sort()
print(*numberlist[:1])
print(min(numberlist))

# find the maximum number from the list

userinput = int(input("enter number of elements in a list: "))
print(userinput)
emptylist = []
for item in range(0, userinput):
    uservalue = int(input("enter element: "))
    emptylist.append(uservalue)
print("The maximum value in list is",  max(emptylist))
print("The maximum value in list is",  max(emptylist))

# second maximum number
# use the [-2]

numberlist = [12, 0, 89, -12, 67, 90, 0]
numberlist.sort()
print("The second maximum number is", numberlist[-2])


# find the max number from the list then rempove that element from thr list. Again find the maximum number

def maxnumber(numberlist):
    numberlist.sort()
    newlist = numberlist
    newlist.remove(max(numberlist))
    print("The second largest number in a list is :", max(newlist))
    return newlist
numberlist = [12, 0, 89, -12, 67, 90, 0]
maxnumber(numberlist)


# Python program to find N largest elements from a list

numberslist = [12, 1000, -990, 89, -12, 6, 0, 230, 8]
nelements = 2
count = 0
numberslist.sort()
for number in range (len(numberslist)):
    for value in range(number+1,len(numberslist) ):
        if numberslist[value] > number:
            number = numberslist[value]
print(number)


# Python program to print Even Numbers in given range


number1 = int(input("Enetr your number range starts from: "))
number2 = int(input("Enetr your number range ends: "))
for item in range(number1, number2 +1 ):
    if item %2 == 0:
        print(item, end = " ")


# Python program to print positive numbers in a list
numberlist = [12, -90, -45, -76, 0, 12, 3, 67]
for item in numberlist:
    if item >= 0:
         print(item)

# method 2 filter()
#
numberlist = [12, -90, -45, -76, 0, 12, 3, 67]
lambdalist = filter(lambda x: x <=0 , numberlist)
for item in lambdalist:
    print(item,  end = " ")


# print all negative numbers in a range
startnumber = -10
endnumber = 10
for item in range(startnumber, endnumber +1 ):
    if item < 0:
        print(item, end = " ")

# count positive and negative numbers in a list
numbrelist = [-0.89, 67, 89, -15, -100, 33, 89, -54, 900, 6789]
positive = 0
negative = 0
for item in numbrelist:
     if item < 0:
         negative = negative + 1
     else:
         positive = positive + 1
print("The negative numbers count:", negative)
print("The positive numbers count:", positive)

# Remove multiple elements from a list in Python
selectnumber = int(input("Please enter the element you want to remove from list: "))
numberslist = [15, 67, 0, 89, 80, 5564, 0, 355]
removelist = []
remaininglist = []
for item in numberslist:
    if item != selectnumber:
        print(item, end=" ")

 Remove empty tuples from a list
def emptytuple(tuplelist):
    emptylist = [  item for item in tuplelist if item]
    return  emptylist
tuplelist = [(12, 34, 56), (), (89, -890), 90, 553, 23, 657, ('', ''), (0), 0, ('none') ]
print(emptytuple(tuplelist))


#Python program to find Cumulative sum of a list

numOfElemenets = int(input("numbe of elements you want in list: "))
elements= []
emptylist = []
firstValue = 0
while numOfElemenets > 0:
    element = int(input("enter your element: "))
    elements.append(element)
    numOfElemenets -= 1
for item in range(len(elements)):
    firstValue = firstValue +  elements[item]
    emptylist.append(firstValue)
print(emptylist)

# take an input from user and perform the below operations to return Boolean value
def greaterthan(x, y):
    return x > y

def lessthan(x, y):
    return x < y

def equal(x, y):
    return x == y

isContinue = True
while isContinue:
    elementOne = input("Enter your first element \noptions are  1. integer 2. float 3. string : ")
    print("available operations \n1. < \n2. = , \n3. >")
    operation = input("Enter your operator: ")
    isValidOperation = False
    while not isValidOperation:
        if operation not in ['>', '<', '=']:
            operation = input("Operator is not valid. select your operation type from the above options")
        else:
            isValidOperation = True

    elementTwo = input("enter your second element: \noptions are  1. integer 2. float 3. string : ")

    if operation == '>':
        print(greaterthan(elementOne, elementTwo))
    elif operation == '<':
        print(lessthan(elementOne, elementTwo))
    elif operation == '=':
        print(equal(elementOne, elementTwo))
    else:
        print("operation can not be done, wrong inputs")

    if input("Do you want to continue(y/n): ") == 'n':
        isContinue = False
