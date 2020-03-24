# print all elements of a list using for loop.
"""
list=[1.1,2.2, -3,-1, '5k', "abs", "agdh"]
for no in list:
    print(no)

2) Take inputs from user to make a list.
Again take one input from user and search it in the list and delete that element, if found.
Iterate over list using for loop.


li=[2,3,5,6,7]
l2= [2,3,10,6,8]
l3=[]
for x in li:
    #print(x)
    if x in l2:
        l3.append(x)
    else:
        print(" uncommeon elemets in two lists are", x)
#print("Uncommon elements are: ", x)
print("Common elements in two lists are" , l3)

def sa(l1,l2):
    ab=set(l1)
    bc=set(l2)
    if (ab & bc):
        print("The coomon are:", set(l1) & set(l2))
l1= [2, 3, 5, 6, 7]
l2 = [2, 3, 10, 6, 8]
sa(l1,l2)

# print the multiplication of input numbe
n=int(input("enter integer number: "))
for i in range(1,11):
    print(n, 'x', i, '=', n*i)

Print multiplication table of 14 from a list in which multiplication table of 12 is stored.

# take the multiplcation of table
n=int(input("enter integer number: "))
n12=[]
for i in range(1,11):
    x= n*i
    n12.append(x)
print(n12)
You are given with a list of integer elements. Make a new list which will store square of elements of previous list.

#Using range(1,101), make two list, one containing all even numbers and other containing all odd numbers.

evlist=[]
odlist=[]
for x in range(1,101):
    if x%2==0:
        evlist.append(x)
    else:
        odlist.append(x)
print("The even numbers list is: ", evlist)
print("The odd numbers list is: ", odlist)


#n=int(input("enter integer number: "))

#44. Write a Python program to construct the following pattern, using a nested loop number.
for x in range (1,10):
    print(str(x)*x)
"""

tu=(100,200,300)
print(type(tu))
# to string fromat
print(" the string format {0} is", format(tu))