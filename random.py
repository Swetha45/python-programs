
#    find  a number which is replaced by zero

import random
def randomnumber(list1):
    sum1 = 0
    for item in list1:
        sum1 = sum1 + item
    print("The sum of first list is to be: ", sum1)
    index = random.randint(0, len(list1) - 1)
    list1[index] = 0
    print("After making chnages list1 is: ", list1)
    sum2 = 0
    for item in list1:
        sum2 = sum2 + item
    print("The sum of after making changes list is :", sum2)
    difference = sum1 - sum2
    print("The number the set to index is: ", difference )
    return list1
list1 = [1, 9, 19, 10, 70]
print("The original list: ", list1)
randomnumber(list1)