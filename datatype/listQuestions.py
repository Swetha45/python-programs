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


