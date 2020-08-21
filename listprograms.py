# find the duplicates form the list

numberslist = [2,2,3,4,11,9,11,10]
duplicatelist = []
for number in range (len(numberslist)):
    for value in range(number+1,len(numberslist) ):
        if( numberslist[number] == numberslist[value]):
            duplicatelist.append(numberslist[value])
print("The duplicate values in the list:", duplicatelist)

# count the duplicate element in a list

list1 = [2, 2, 3, 4, 11, 9, 11, 10]
dictvalue = dict()
indexDict = dict()
#
for value in list1:
    indexList = []
    if value in dictvalue:
        dictvalue[value] += 1
        if value in indexDict:
            indexList = indexDict[value]
    else:
        dictvalue[value] = 1
    if not indexList:
        indexList.append(list1.index(value))
    else:
        indexList.append(list1.index(value, (indexList[len(indexList)-1]+1)))
    indexDict[value] = indexList
for key, value in dictvalue.items():
    if value > 1:
        print("total count of repeated elements are:", key, ':', value)
for key, value in indexDict.items():
    if len(value) > 1:
        print("Indexes of repeated elements are:", key, ':', value)



#Check if element exists in list in Python

nameslist = ["School", "Teacher", "Employee", "Office"]
element = "School"
for name in nameslist:
    if name in element:
        print("The element '{}' is exists in list". format(element))


# how to clear a list in python

#  Reversing a List

#reversed()

numberslist = [10,20,30, 40, 50]
for number in reversed(numberslist):
    print(number)


#reverse()
#
numberslist = [10, 20,30, 40, 50]
rever = numberslist.reverse()
print(list1)

# slicing
def reversenumber(numberslist):
    reversevalue = numberslist[::-1]
    return reversevalue

numberslist = [10, 20, 30, 40, 20]
print(reversenumber(numberslist))


#  Cloning or Copying a list
# method 1:append


numbers = [0, -1, "python", 100, "reading", "practice"]
integerlist = []
stringlist = []
for values in numbers:
    if isinstance(values, int):
        integerlist.append(values)
    elif type(values) == str:
     stringlist.append(values)
print("The original list is", numbers )
print("The integer values from a list", integerlist)
print("The remaining values in list1 are", stringlist )

# method 1:extend

firstnumberlist = [-1, 10, 90, 0.0333, "python", "reading", [12, 10, 87, 466]]
secondnumberlist = [0, -1999, 3, 10]
secondnumberlist.extend(firstnumberlist)
print(secondnumberlist)


#method 3 list

firstnumberlist = [12,90,89,0.789, 34]
secondnumberlist = []
secondnumberlist = firstnumberlist
copyvalues = list(secondnumberlist)
print(secondnumberlist)

# method4 copy()
firstnumberlist = [12, 90, 89, 0.789, 34]
secondnumberlist = []
copyvalues = firstnumberlist.copy()
secondnumberlist = copyvalues
print(secondnumberlist)


# Count occurrences of an element in a list

numberslist = [12,2,12, 45,12, 2,3,2,12,12, 45]
number = 12
count = 0
for values in numberslist:
    if values == number:
        count = count + 1
print("The number {} appeared {} time(s) in a list".format(number, count))

# Counter
from collections import Counter
numberslist = [12, 2, 12, 45,12, 2,3,2,12,12, 45]
number = 12
countervalue = Counter(list1)
print("The number {} appeared {} time(s) in a numberslist".format(number, countervalue[number]))

# sum of elements in list
# method1 : sum()

def sumvalues(numberslist):
        totalnumber = sum(numberslist)
        print("The total sum of elements in a list:", totalnumber)
        return totalnumber
numberslist = [12,4, -12, 90, 78, 45]
sumvalues(list1)

# method2
# for and if

numberslist = [12, 4, 90, 78, 45]
count = 0
for values in range(0, len(numberslist)):
        count = count + numberslist[values]
print(count)

#Multiply all numbers in the list
# method 1

numberslist = [1, 2, 3, 4, 5, 10, -10, 10.9, "python", "Test"]
count = 1
list2 = []
for value in numberslist:
    if type(value) == int or type(value) == float:
        count = count * value
print(count)


# method 2 math.prod
import math
valuelist = [12, 90, 67, -23, 0.780]
for item in valuelist:
    if type(item) == int or type(item) == float:
        multiply = math.prod(valuelist)
print("The result is", multiply)



#Lambda function


from functools import reduce
valuelist = [12, 90, 67, -23, 2]

reducefunc = reduce((lambda value1, value2:value1* value2), valuelist)
print("Result is:", reducefunc )