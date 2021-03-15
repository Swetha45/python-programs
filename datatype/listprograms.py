# 1Q: Find the duplicates form the list

numberslist = [2,2,3,4,11,9,11,10]
duplicatelist = []
for number in range (len(numberslist)):
    for value in range(number+1,len(numberslist) ):
        if( numberslist[number] == numberslist[value]):
            duplicatelist.append(numberslist[value])
print("The duplicate values in the list:", duplicatelist)

# 2Q: Count the duplicate element in a list

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


# 3Q: Check if element exists in list in Python

nameslist = ["School", "Teacher", "Employee", "Office"]
element = "School"
for name in nameslist:
    if name in element:
        print("The element '{}' is exists in list". format(element))


#4Q: How to reverse a list in python
        # Method 1 reversed() function

numberslist = [10,20,30, 40, 50]
for number in reversed(numberslist):
    print(number)

   # Method 2 using reverse()
numberslist = [10, 20,30, 40, 50]
rever = numberslist.reverse()
print(list1)

    # Method 3 slicing
def reversenumber(numberslist):
    reversevalue = numberslist[::-1]
    return reversevalue
numberslist = [10, 20, 30, 40, 20]
print(reversenumber(numberslist))


# 5Q:  Cloning or Copying a list
       # method 1: append method
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

        # Method 2: extend method

firstnumberlist = [-1, 10, 90, 0.0333, "python", "reading", [12, 10, 87, 466]]
secondnumberlist = [0, -1999, 3, 10]
secondnumberlist.extend(firstnumberlist)
print(secondnumberlist)
        # Method 3: list function

firstnumberlist = [12,90,89,0.789, 34]
secondnumberlist = []
secondnumberlist = firstnumberlist
copyvalues = list(secondnumberlist)
print(secondnumberlist)

        # Method 4:  copy() method
firstnumberlist = [12, 90, 89, 0.789, 34]
secondnumberlist = []
copyvalues = firstnumberlist.copy()
secondnumberlist = copyvalues
print(secondnumberlist)


# 6Q: Count occurrences of an element in a list

numberslist = [12,2,12, 45,12, 2,3,2,12,12, 45]
number = 12
count = 0
for values in numberslist:
    if values == number:
        count = count + 1
print("The number {} appeared {} time(s) in a list".format(number, count))

    # method 1:  Counter
from collections import Counter
numberslist = [12, 2, 12, 45,12, 2,3,2,12,12, 45]
number = 12
countervalue = Counter(list1)
print("The number {} appeared {} time(s) in a numberslist".format(number, countervalue[number]))

# 7Q: sum of elements in list
       # Method1 : using sum() function

def sumvalues(numberslist):
        totalnumber = sum(numberslist)
        print("The total sum of elements in a list:", totalnumber)
        return totalnumber
numberslist = [12,4, -12, 90, 78, 45]
sumvalues(list1)

        # Method2: for and if

numberslist = [12, 4, 90, 78, 45]
count = 0
for values in range(0, len(numberslist)):
        count = count + numberslist[values]
print(count)

# 8Q: Multiply all numbers in the list
       # method 1

numberslist = [1, 2, 3, 4, 5, 10, -10, 10.9, "python", "Test"]
count = 1
list2 = []
for value in numberslist:
    if type(value) == int or type(value) == float:
        count = count * value
print(count)
            # Method 2 math.prod
import math
valuelist = [12, 90, 67, -23, 0.780]
for item in valuelist:
    if type(item) == int or type(item) == float:
        multiply = math.prod(valuelist)
print("The result is", multiply)

    # method 3: Lambda function

from functools import reduce
valuelist = [12, 90, 67, -23, 2]

reducefunc = reduce((lambda value1, value2:value1* value2), valuelist)
print("Result is:", reducefunc )

# 9Q: Python program to find smallest number in a list

numberlist = [12, 0, 89, -12, 67, 90, 0]
numberlist.sort()
print(*numberlist[:1])
print(min(numberlist))

#10Q: Find the maximum number from the list

userinput = int(input("enter number of elements in a list: "))
print(userinput)
emptylist = []
for item in range(0, userinput):
    uservalue = int(input("enter element: "))
    emptylist.append(uservalue)
print("The maximum value in list is",  max(emptylist))
print("The maximum value in list is",  max(emptylist))

# 11Q:  Find the second maximum number from the list
       # use the [-2]

numberlist = [12, 0, 89, -12, 67, 90, 0]
numberlist.sort()
print("The second maximum number is", numberlist[-2])

# 12Q: find the max number from the list then rempove that element from thr list. Again find the maximum number

def maxnumber(numberlist):
    numberlist.sort()
    newlist = numberlist
    newlist.remove(max(numberlist))
    print("The second largest number in a list is :", max(newlist))
    return newlist
numberlist = [12, 0, 89, -12, 67, 90, 0]
maxnumber(numberlist)


# 13Q: Python program to find N largest elements from a list

numberslist = [12, 1000, -990, 89, -12, 6, 0, 230, 8]
nelements = 2
count = 0
numberslist.sort()
for number in range (len(numberslist)):
    for value in range(number+1,len(numberslist) ):
        if numberslist[value] > number:
            number = numberslist[value]
print(number)


# 14Q: Python program to print Even Numbers in given range

number1 = int(input("Enetr your number range starts from: "))
number2 = int(input("Enetr your number range ends: "))
for item in range(number1, number2 +1 ):
    if item %2 == 0:
        print(item, end = " ")

# 15Q: Python program to print positive numbers in a list
numberlist = [12, -90, -45, -76, 0, 12, 3, 67]
for item in numberlist:
    if item >= 0:
         print(item)

     # Method 2: using filter() method

numberlist = [12, -90, -45, -76, 0, 12, 3, 67]
lambdalist = filter(lambda x: x <=0 , numberlist)
for item in lambdalist:
    print(item,  end = " ")

# 16Q: Print all negative numbers in a range
startnumber = -10
endnumber = 10
for item in range(startnumber, endnumber +1 ):
    if item < 0:
        print(item, end = " ")

# 17Q: Count positive and negative numbers in a list

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

# 18Q: Remove multiple elements from a list in Python

selectnumber = int(input("Please enter the element you want to remove from list: "))
numberslist = [15, 67, 0, 89, 80, 5564, 0, 355]
removelist = []
remaininglist = []
for item in numberslist:
    if item != selectnumber:
        print(item, end=" ")

# 19Q: Remove empty tuples from a list

def emptytuple(tuplelist):
    emptylist = [  item for item in tuplelist if item]
    return  emptylist
tuplelist = [(12, 34, 56), (), (89, -890), 90, 553, 23, 657, ('', ''), (0), 0, ('none') ]
print(emptytuple(tuplelist))


# 20Q: Python program to find Cumulative sum of a list

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

# 21Q: Take an input from user and perform the below operations to return Boolean value

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

# 22Q: Sum of all the items in list

sumList = [10, 80, -90, 0, -25, 33, 865]
sum = 0
for item in sumList:
    sum = item + sum
print("The sum of list", sum)

# 23Q. Print largest number of list

list1 = [-79, 0, 573.78, 899, -34, 23.88]
list1.sort()
print('The largest number in list is: ' , list1[-1])
print('The smallest number in list is: ', list1[0])

# 24Q:.Count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

listElements = ['python' , 89, -5667, 0.789, 'excercise', 'list', 'programs', 'abcda', '1231']
count = 0
listString = [item for item in listElements if isinstance(item, str)]
for stringitem in listString:
    if len(stringitem) >= 2 and stringitem[0] == stringitem[-1]:
        count = count + 1
print('The number of strings:' , count)

# 25Q: Remove duplicate elements form list

list1 = [10, 10, -20, 30, 10, 180, 20, -20]
list2 = []
for item in list1:
    if item not in list2:
        list2.append(item)
print('After removing the duplicates, the current list is:' , list2)

# 26Q: Python program to check a list is empty or not

currentlist = [1,2]
if not currentlist:
    print('The list is empty')
else:
    print('The list is not empty')


# 27Q: Find the list of words that are longer than n from a given list of words

wordsList = ['I', 'am', 'learning', 'python', '3', '123']
n = 3
newList = []
for word in wordsList:
    if len(word) >= n:
        newList.append(word)
print('The list of words longer than n is :', newList)

# 28Q: Write a Python function that takes two lists and returns True if they have at least one common member.

def fruitslist(list1, list2):
    result = False
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                result = True
    return result
list1 = ['apple', 'banana', 'oranges', 'grape']
list2 = ['grape', 'strawberry', 'peach', 'cherry', 'apple']
print('The common items from two list is: ', fruitslist(list1, list2))

# 29Q: Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

colorList = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colorList = [item for index, item in enumerate(colorList) if index not in (0,4,5)]
print('After removing the 0th, 4th and 5th elements, list is :', colorList )

# 30Q: Shuffle the number and print the result

from random import shuffle
list1 = [1,2,3,4,5,6,7,8,9,20]
shuffle(list1)
print('After shuffling, the number is ', list1)

# 31Q: Provide permutations and combinations of list

from itertools import permutations
from itertools import combinations
permutation_list = permutations([1, 2, 3,4,5], 2)
combination_list = combinations([1, 2, 3,4,5], 3)
for item1 in list(permutation_list):
    print('the permuations of given list: ', item1)
for item2 in list(combination_list):
    print('the combinations of given list: ', item2)

# 32Q: Convert a list of characters into a string

wordsList = ['a', 'b', 'c', 'd']
stringList = ''.join(wordsList)
print(stringList)

# 33Q: Index of an item in a specified list.

list1 = [10, 10, -20, 30, 10, 180, 20, -20]
print('The first index of an item: ', list1[0])
print('The last index of an item: ', list1[-1])
print('The index of 30: ', list1.index(30))
print('The index of 10: ', list1.index(10, 0, len(list1) ))
index_pos = 0
new_value = -20
index_list = []
for index in range(len(list1)):
    if list1[index] == new_value:
        index_list.append(index)
print("the indexes of 10 is : ", index_list )

# 34Q: shallow list

import itertools
first_list = [[22,4,30],['pyhton', 'program'], [-9], [0.7,9,0]]
second_list = ['pyhton', 'program']
new_merged_list1 = list(itertools.chain(*first_list))
new_merged_list2 = tuple(itertools.chain(*second_list))
print(new_merged_list1)
print(new_merged_list2)

# 35Q: Select random item from list

import random
fruits_list = ['banana', 'apple', 'grape', 'peach', 'orange']
random_fruit = random.choice(fruits_list)
print('The random fruit from fruit list: ', random_fruit)

# 36Q: Check whether two lists are circularly identical

list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
str1 = ''
str2 = ''
for item1 in list1:
    str1 = str1 + str(item1)
for item2 in list2:
    str2 = str2 + str(item2)
if str2 in str1 *2:
    print('true')
else:
    print('false')

# 37Q: Find the second smallest number in a list.

list1 = [10, -233, 90, 0, -354, -4.55, 0.455]
list1.sort()
print('The second smallest number in a list', list1[1])

# 38Q: Write a Python program to shuffle and print a specified list.

from random import shuffle
colrs_List = ['orange', 'blue', 'pink', 'white', 'yellow', 'pink']
shuffle(colrs_List)
print('After suffling the list: ', colrs_List )
shuffle(colrs_List)
print('After re-suffling the list: ', colrs_List )

# 39Q: Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

start_value = int(input("What is start range of list: "))
end_value =   int(input("What is end range of list: "))
first_five = []
last_five = []
if (start_value >=1 and end_value <= 30) and (end_value > start_value and end_value - start_value > 10):
        for index1 in range(start_value, start_value + 5):
           first_five.append(index1 *2)
        for index2 in range(end_value - 5, end_value):
            last_five.append(index2 * 2)
        print('Sqaure of first five elements', first_five)
        print('Sqaure of last five elements', last_five)
else:
    print("The range of elements in list should be between 1 and 30 and diff should be > 10")

# 40Q: How to remove duplicate items from list

duplicate_list = [10, 20 , 20, 30, 10, -100, -22, -100, 10]
set_list = set(duplicate_list)
print(list(set_list))

# 41Q: Python program to get the frequency of the elements in a list.

from collections import Counter
duplicate_list = [10, 20 , 20, 30, 101, -100, -22, -100, 10]
count_element = Counter(duplicate_list)
print('The frequency of the elements in a list', count_element)
for element in count_element.elements():
    print(element)
for element1 in count_element.most_common(2):
    print("The most common element in list: ", element1)

# 42Q: Create a list by concatenating a given list which range goes from 1 to n.

my_list = ['a', 'b']
n= 4
new_list = ['{}{}'.format(item, index) for index in range(1, n+1)  for item in my_list ]
print(new_list)

# 43Q: Write a Python program to get variable unique identification number or string.

colrs_List = ['orange', 'blue', 'pink', 'white', 'yellow', 'pink', 'black']
unique_id = id(colrs_List)
print(unique_id)

# 44Q: Write a Python program to find common items from two lists.

color_list11 = ["Red", "Green", "Orange", "White", "Black"]
color_list2 = ["Black", "Green", "White", "Pink"]
set1 = set(color_list11)
set2 = set(color_list2)
print('The common elements form list: ', set1&set2)
print('The common elements form list: ', set1.intersection(set2))

# 45Q: Write a Python program to change the position of every n-th value with the (n+1)th in a list.

def mylist(list1):
    for index in range(0, len(list1), 2):
        list1[index], list1[index+1] = list1[index+1], list1[index]
        return list1
list1 = [10, 20, 30, 40, 50]
mylist(list1)
print('The current list: ', list1)

# 46Q: Python program to convert a list of multiple integers into a single integer.

integer_list = [10, 20, 30]
print("type of interger list: ", type(integer_list))
convert_string = ''.join(map(str, integer_list))
print('The result is: {}'.format(convert_string))
print("type of interger list: ", type(convert_string))


# 47Q: Python program to split a list based on first character of word.

from itertools import groupby
from operator import itemgetter
name_lists = ['abc', 'python', 'bca', 'aab', 'swetha', 'sam' ]
for name, words in groupby(sorted(name_lists), itemgetter(0)):
    for word in words:
        print('Splited list by furst character: \"{}\"  of the list: \"{}\" ' .format(name, word))
