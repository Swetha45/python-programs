# 1. Python program to count number of vowels using sets in given string

string = "Hello World"
vowels = set('AEIOUaeiou')
count = 0
for item in string:
    if item in vowels:
        count = count + 1
print("The no of vowels in a given string is:", count)


# 2. Remove all duplicates from a given string in Python

string = "geeksforgeeks"
count = 0
emptystring = ""
for item in string:
    if item in emptystring:
        pass
    else:
        emptystring = emptystring + item
print("After removing the duplicates: ", emptystring)

# 3. Program to check if a string contains any special character
import re
def specialcharacter(text):
    character = re.compile("[!@#$%^&*()+_{}?/.>]")
    if character.search(text) == None:
        print("no special characters")
    else:
        print("sting have special characters" )
text = "PYT@n@pR*g#m!n+"
specialcharacter(text)

# 4. Find words which are greater than given length k
string = "I am begginer in programming"
splitstring = string.split()
emptystring = []
length = 4
for text in splitstring:
   if len(text) > length:
       emptystring.append(text)
print(emptystring)

# Python program for removing i-th character from a string

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


# method 2 use replace

def repalcestring(string):
    characterIndex = int(input("Enter your index number: "))
    for char in range (len(string)):
        if char == characterIndex:
            string = string.replace(string[char], "")
    return string
if __name__ == '__main__':
    string = "Python programs"
print(repalcestring(string))

# Python program to split and join a string

string = "am beginner in python program. like to learn python"
splittext = string.split(" ")
jointext = " == ".join(splittext)
print(jointext)
print(splittext)

#  Check if a given string is binary string or not

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

# Find all close matches of input string from a list
# mthod 1: get_close_matches

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

# method 2

string1 = 'learn python. practice python'
string2 =  "am Learning python by myself"
splitstring1 = string1.split()
splitstring2 = string2.split()
difference = set(splitstring1).symmetric_difference(set(splitstring2))
print("The uncommon words from two strings:",difference )



# Swap commas and dots in a String

string = "123, -905. 23112, -789002"
string = string.replace(', ', 'comma')
string = string.replace('.', ', ')
string = string.replace('comma', '.')
print(string)

# permuataion and combinations of a string
from itertools import permutations, combinations

string = 'ABC'
permutationstring = permutations(string)
combinationstring = combinations(string, 3)
for permutat in list(permutationstring):
    print("The permutation ", ' '.join(permutat))
for combt in list(combinationstring):
    print("The combination: ", ' '.join(combt))