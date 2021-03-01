# 1 . Sum of all the items in list

sumList = [10, 80, -90, 0, -25, 33, 865]
sum = 0
for item in sumList:
    sum = item + sum
print("The sum of list", sum)

#2. print largest number of list

list1 = [-79, 0, 573.78, 899, -34, 23.88]
list1.sort()
print('The largest number in list is: ' , list1[-1])
print('The smallest number in list is: ', list1[0])

# 3.  count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings

listElements = ['python' , 89, -5667, 0.789, 'excercise', 'list', 'programs', 'abcda', '1231']
count = 0
listString = [item for item in listElements if isinstance(item, str)]
for stringitem in listString:
    if len(stringitem) >= 2 and stringitem[0] == stringitem[-1]:
        count = count + 1
print('The number of strings:' , count)

#4. Remove duplicate elements form list

list1 = [10, 10, -20, 30, 10, 180, 20, -20]
list2 = []
for item in list1:
    if item not in list2:
        list2.append(item)
print('After removing the duplicates, the current list is:' , list2)

#5. Python program to check a list is empty or not

currentlist = [1,2]
if not currentlist:
    print('The list is empty')
else:
    print('The list is not empty')


# 6.  find the list of words that are longer than n from a given list of words

wordsList = ['I', 'am', 'learning', 'python', '3', '123']
n = 3
newList = []
for word in wordsList:
    if len(word) >= n:
        newList.append(word)
print('The list of words longer than n is :', newList)

# 7. Write a Python function that takes two lists and returns True if they have at least one common member.

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

# 8. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

colorList = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
colorList = [item for index, item in enumerate(colorList) if index not in (0,4,5)]
print('After removing the 0th, 4th and 5th elements, list is :', colorList )

# 9. shuffle the number and print the result

from random import shuffle
list1 = [1,2,3,4,5,6,7,8,9,20]
shuffle(list1)
print('After shuffling, the number is ', list1)

#10. Provide permutations and combinations of list

from itertools import permutations
from itertools import combinations
permutation_list = permutations([1, 2, 3,4,5], 2)
combination_list = combinations([1, 2, 3,4,5], 3)
for item1 in list(permutation_list):
    print('the permuations of given list: ', item1)
for item2 in list(combination_list):
    print('the combinations of given list: ', item2)

# 11. convert a list of characters into a string

wordsList = ['a', 'b', 'c', 'd']
stringList = ''.join(wordsList)
print(stringList)

# 12. index of an item in a specified list.

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


# 13. shallow list

import itertools
first_list = [[22,4,30],['pyhton', 'program'], [-9], [0.7,9,0]]
second_list = ['pyhton', 'program']
new_merged_list1 = list(itertools.chain(*first_list))
new_merged_list2 = tuple(itertools.chain(*second_list))
print(new_merged_list1)
print(new_merged_list2)


# 14. select random item from list

import random
fruits_list = ['banana', 'apple', 'grape', 'peach', 'orange']
random_fruit = random.choice(fruits_list)
print('The random fruit from fruit list: ', random_fruit)

# 15. Check whether two lists are circularly identical

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

# 16. find the second smallest number in a list.

list1 = [10, -233, 90, 0, -354, -4.55, 0.455]
list1.sort()
print('The second smallest number in a list', list1[1])

# 17. Write a Python program to shuffle and print a specified list.

from random import shuffle
colrs_List = ['orange', 'blue', 'pink', 'white', 'yellow', 'pink']
shuffle(colrs_List)
print('After suffling the list: ', colrs_List )
shuffle(colrs_List)
print('After re-suffling the list: ', colrs_List )

 # 18. Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).

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


#19 . How to remove duplicate items from list

duplicate_list = [10, 20 , 20, 30, 10, -100, -22, -100, 10]
set_list = set(duplicate_list)
print(list(set_list))

# 20.  Python program to get the frequency of the elements in a list.

from collections import Counter
duplicate_list = [10, 20 , 20, 30, 101, -100, -22, -100, 10]
count_element = Counter(duplicate_list)
print('The frequency of the elements in a list', count_element)
for element in count_element.elements():
    print(element)
for element1 in count_element.most_common(2):
    print("The most common element in list: ", element1)

# 21. create a list by concatenating a given list which range goes from 1 to n.

my_list = ['a', 'b']
n= 4
new_list = ['{}{}'.format(item, index) for index in range(1, n+1)  for item in my_list ]
print(new_list)

# 22. Write a Python program to get variable unique identification number or string.

colrs_List = ['orange', 'blue', 'pink', 'white', 'yellow', 'pink', 'black']
unique_id = id(colrs_List)
print(unique_id)

#23.Write a Python program to find common items from two lists.

color_list11 = ["Red", "Green", "Orange", "White", "Black"]
color_list2 = ["Black", "Green", "White", "Pink"]
set1 = set(color_list11)
set2 = set(color_list2)
print('The common elements form list: ', set1&set2)
print('The common elements form list: ', set1.intersection(set2))

# 24. Write a Python program to change the position of every n-th value with the (n+1)th in a list.

def mylist(list1):
    for index in range(0, len(list1), 2):
        list1[index], list1[index+1] = list1[index+1], list1[index]
        return list1
list1 = [10, 20, 30, 40, 50]
mylist(list1)
print('The current list: ', list1)

# 25. Python program to convert a list of multiple integers into a single integer.

integer_list = [10, 20, 30]
print("type of interger list: ", type(integer_list))
convert_string = ''.join(map(str, integer_list))
print('The result is: {}'.format(convert_string))
print("type of interger list: ", type(convert_string))


# 26. Python program to split a list based on first character of word.

from itertools import groupby
from operator import itemgetter
name_lists = ['abc', 'python', 'bca', 'aab', 'swetha', 'sam' ]
for name, words in groupby(sorted(name_lists), itemgetter(0)):
    for word in words:
        print('Splited list by furst character: \"{}\"  of the list: \"{}\" ' .format(name, word))