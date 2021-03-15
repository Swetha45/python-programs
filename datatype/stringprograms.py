# 1Q: Python program to count number of vowels using sets in given string

string = "Hello World"
vowels = set('AEIOUaeiou')
count = 0
for item in string:
    if item in vowels:
        count = count + 1
print("The no of vowels in a given string is:", count)


# 2Q: Remove all duplicates from a given string in Python

string = "geeksforgeeks"
count = 0
emptystring = ""
for item in string:
    if item in emptystring:
        pass
    else:
        emptystring = emptystring + item
print("After removing the duplicates: ", emptystring)

# 3Q: Program to check if a string contains any special character

import re
def specialcharacter(text):
    character = re.compile("[!@#$%^&*()+_{}?/.>]")
    if character.search(text) == None:
        print("no special characters")
    else:
        print("sting have special characters" )
text = "PYT@n@pR*g#m!n+"
specialcharacter(text)

# 4Q: Find words which are greater than given length k

string = "I am begginer in programming"
splitstring = string.split()
emptystring = []
length = 4
for text in splitstring:
   if len(text) > length:
       emptystring.append(text)
print(emptystring)

# 5Q: Python program for removing i-th character from a string

text = "Python programs"
characterIndex = int(input("Enter your index number: "))
newstring = ""
if len(text) >= characterIndex:
    for char in range(len(text)):
            if char != characterIndex:
                newstring = newstring + text[char]
    print("After removing the ith character the result is: ", newstring)
else:
    print("index is out of range")

   # Method 2: using replace() method

def repalcestring(string):
    characterIndex = int(input("Enter your index number: "))
    for char in range (len(string)):
        if char == characterIndex:
            string = string.replace(string[char], "")
    return string
if __name__ == '__main__':
    string = "Python programs"
print(repalcestring(string))

# 6Q: Python program to split and join a string

string = "am beginner in python program. like to learn python"
splittext = string.split(" ")
jointext = " == ".join(splittext)
print(jointext)
print(splittext)

# 7Q: Check if a given string is binary string or not

string = "00000222-1111010s"
binaryvalues= ['0', '1']
count = 0
for char in string:
    if char not in binaryvalues:
        count = count + 1
if count:
    print("The string {} is not a binary string".format(string) )
else:
    print("binary string")

# 8Q: Find all close matches of input string from a list
      # Method 1: using get_close_matches function

from difflib import get_close_matches
string = ['comp', 'compuuteeer', 'laptop', 'puter']
matchword = 'computer'
findMatches = get_close_matches(matchword, string)
print(findMatches)

string1 = 'learn python. practice python'
string2 = "am Learning python by myself"
uncommonString = " "
splitstring1 = string1.split()
splitstring2 = string2.split()
for word1 in splitstring1:
    if word1 not in splitstring2:
        uncommonString = uncommonString + ' ' + word1
for word2 in splitstring2:
    if word2 not in splitstring1:
        uncommonString = uncommonString + ' ' + word2
print("The uncommon words from two strings:", uncommonString)

            # Method 2: using split() method

string1 = 'learn python. practice python'
string2 =  "am Learning python by myself"
splitstring1 = string1.split()
splitstring2 = string2.split()
difference = set(splitstring1).symmetric_difference(set(splitstring2))
print("The uncommon words from two strings:",difference )

# 9Q: Swap commas and dots in a String

string = "123, -905. 23112, -789002"
string = string.replace(', ', 'comma')
string = string.replace('.', ', ')
string = string.replace('comma', '.')
print(string)

# 10Q: Permuataion and combinations of a string
from itertools import permutations, combinations

string = 'ABC'
permutationstring = permutations(string)
combinationstring = combinations(string, 3)
for permutat in list(permutationstring):
    print("The permutation ", ' '.join(permutat))
for combt in list(combinationstring):
    print("The combination: ", ' '.join(combt))

# 11Q: How to reverse order of string?
     # Method 1: [::-1]
def palindome(string):
    return string == string[::-1]
string = input("Enter your palindrome string: ")
result = palindome(string)
if result :
    print("The string is palindrome")
else:
    print("The string is not palindrome")

     # Method 2:  .join(reversed(string))

userstring = input("Enter your palindrome string: ")
reverevalue = ''.join(reversed(userstring))
if reverevalue == userstring:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
list = [1,2,3]
list.reverse()

      # Method 3: for loop

userstring = input("Enter your palindrome string: ")
emptystring = ""
for letter in userstring:
    emptystring = letter + emptystring
    if (emptystring == userstring):
        print("The string is palindrome")
        break
else:
    print("The string is not palindrome")

# 12Q: How to reverese a sentence

userstring = "I am interested in Python3"
splitword = userstring.split()
reversestring = ' '.join(reversed(splitword))
print(" The userstring is:  " + userstring + "\n after reversing the result is:  " + reversestring)

#  12Q: Remove i’th character from string in Python

try:
    userstring = "pythonProgram"
    userinput = int(input("Please enter your character position: "))
    emptystring = ""
    if len(userstring) >= userinput:
        for character in range(len(userstring)):
            if userinput != character:
                emptystring = emptystring + userstring[character]
        print("After removing i’th character from string: ",  emptystring)
    else:
        print("The character position is out of string length ")
except ValueError:
   print("Not valid. Please enter integer position of string")

# 13Q: slices

userstring = "pythonProgram"
stringslices = userstring[7:] + userstring [-1: 6]
print(stringslices)

# 14Q: Check if a Substring is Present in a Given String
string1 = 'Python Programs'
string2 = 'Practice Python Programs'
if string2 in string1:
    print("yes")
else:
    print("no")

     # Method 2: using find() method

string1 = 'Python Programs'
string2 = 'Practice Python Programs'
result = string2.find(string1, 4)
if result == -1:
    print("result is not valid")
else:
    print(result)

      # Method 3: Using regular expressions- re.search()

import re
string1 = 'Python Programs'
string2 = 'Practice Python Programs'
if re.search(string1, string2):
    print("The substring: {} is present in the given string: {}".format(string2, string1))
else:
    print("not present")


# 15Q: Convert string into lower cases

vowelsString = "aeiouUUUAAeeIOuII"
lowerstring = vowelsString.lower()
vowels =  set('aeiou')
emptyset = set()
for string in lowerstring:
    if string in vowels:
        emptyset.add(string)

    else:
        pass
if len(emptyset) == len(vowels) :
        print("The string contains all vowels")
else :
   print("The string not contains all vowels")

# 16Q: How do you print duplicate characters from a string? (solution)?

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
       print(name[i])


# 17Q: How do you check if two strings are anagrams of each other?

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


# 18: Write this combinations using input method

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

    # Method 2: recuesive method
def rev(user):
    if len(user)==0:
        return user
    else:
        temp=user[0]
        rev(user[2::])
        print(temp, end="")
user=input("enter a string: ")
rev(user)

# 19Q: How do you check if a string contains only digits?
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

# 20Q: How do you find duplicate characters in a given string?

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

# 21Q: How do you count the occurrence of a given character in a string?
s1= "GeeksforGeeks"
count=0
for char in s1:
   if char in "k":
    count=count+1
print("the total e in string is: ", count)

# 22Q: How do you print the first non-repeated character from a string?

string="iamamswwtha"
a=0
for char in string:
    if string.count(char)>1:
        a=a+1
    else:
        print("only one time", string.count(char))
print("The repitative characters are: ", a)


