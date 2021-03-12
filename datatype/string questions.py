"""def li(a):
    return a[0], a[len(a)-1]
a=[15, 20, 25]
print(li(a))
#fabanocci


# to revere a string
#method 1:
name="swetha"
n=" "
for i in name:
    n = n + i
print("Original string: ", n)
print("After reversing: ", n[::-1])

method 2:
def rev(namee):
    n=" "
    for i in namee:
        n =  n+i
    print("Original string: ", n)
    print("After reversing: ", n[::-1])
namee="swetha"
rev(namee)


#How do you print duplicate characters from a string? (solution)?


name="sweethaasssww"
for i in range(0, len(name)):
   # print("the i values is", i)
    count=1
    for j in range(i+1, len(name)):
        #print("the j values isdsfgh", j)
        #print("hbjhjj", j)

        if (name[i]==name[j]):
            count=count+1
            #print("the count is", count)
    if (count > 1 and name[i]!=0):
       print(name[i]);


 #for integer
a=[3,2,7]
b=sorted(a)
print(b)

#for string
a="swetha"
b=sorted(a)
print(b)
output: ['a', 'e', 'h', 's', 't', 'w']

# if we take two strings
a="swetha", "akshay"
b=sorted(a)
print(b)
output: ['akshay', 'swetha'] because it sort by the first letter in the word

#How do you check if two strings are anagrams of each other?

s1=input("Please enter your  first input: ")
s2=input("Please enter your  second input: ")
if (len(s1)==len(s2)):
    a1=sorted(s1)
    a2=sorted(s2)
    if (a1==a2):
        print("This is anagram")
    else:
        print("This is not an anagram")
else:
    print("The two strings lenghts are not equal. please enter anagram ")

# How do you find all the permutations of a string?
#import a permutations function from the itertools class

from itertools import permutations
def perm(a):
 write that fucntion to list all the elements
    pem= permutations(a)
    print(pem) # create the permutation object
# to print those number
    for x in pem:
        print(''.join(x))
        print(x)
if __name__=='__main__':
    a="ABC"
    perm(a)


#write this combinations usinf input method
combinations formula=

from itertools import combinations
def perm(inn):

    pfun=combinations(inn, 3)
    print(pfun)
    for x in pfun:
        print(''.join(x))
    #print("The total no of permutations are: ", inn.count(pfun))
if __name__=='__main__':
    inn=input("please enter a string: ")
    perm(inn)


#recuesive method
def rev(user):
    if len(user)==0:
        return user
    else:
        temp=user[0]
        rev(user[2::])
        print(temp, end="")
user=input("enter a string: ")
rev(user)

#How do you check if a string contains only digits?
def isd(s1,s2,s3):
    if s1.isdigit():
        print("The given string 1 contails only digits: ", s1.isdigit())
    else:
        print("str 1 is not an integer")
    if s2.isdigit():
        print("The given string 2 contains only digits: ", s2.isdigit())
    else:
        print("str 2 is not an integer")
    if s3.isdigit():
        print("The given string 3 contains only digits: ", s3.isdigit())
    else:
        print("str 3 is not an  integer")
if __name__=='__main__':
    s1=input(" enter string 1:" )
    s2=input(" enter string 2:" )
    s3=input(" enter string 3:" )
    isd(s1,s2,s3)

#How do you find duplicate characters in a given string?
s1="SWETHA@MAN_an"
vowels=0
con=0
for char in s1:
    if char in ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U"):
        vowels=vowels+1
    else:
        con=con+1
print ("The total vowels in a given string is: ", vowels)
print ("The total consonants in a given string is: ", con)

#How do you count the occurrence of a given character in a string?
s1= "GeeksforGeeks"
count=0
for char in s1:
   if char in "k":
    count=count+1
print("the total e in string is: ", count)

#How do you print the first non-repeated character from a string?

#reverse a string first
string="iamamswwtha"
a=0
for char in string:
    if string.count(char)>1:
        a=a+1
    else:
        print("only one time", string.count(char))
print("The repitative characters are: ", a)
"""
# how to removing the character
s1="iamswetha"
print("the original string is: ", s1)
b=s1[:2] + s1[4:]
print("after removing ith position", b)


