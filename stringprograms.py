#methos 1 == reverese order

def palindome(string):
    return string == string[::-1]
string = input("Enter your palindrome string: ")
result = palindome(string)
if result :
    print("The string is palindrome")
else:
    print("The string is not palindrome")


# method 2 --  .join(reversed(string))

userstring = input("Enter your palindrome string: ")
reverevalue = ''.join(reversed(userstring))
if reverevalue == userstring:
    print("The string is palindrome")
else:
    print("The string is not palindrome")
list = [1,2,3]
list.reverse()

# # method 3

userstring = input("Enter your palindrome string: ")
emptystring = ""
for letter in userstring:
    emptystring = letter + emptystring
    if (emptystring == userstring):
        print("The string is palindrome")
        break
else:
    print("The string is not palindrome")

# to reverese a sentence
#
userstring = "I am interested in Python3"
splitword = userstring.split()
reversestring = ' '.join(reversed(splitword))
print(" The userstring is:  " + userstring + "\n after reversing the result is:  " + reversestring)

#  remove i’th character from string in Python

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

# slices

userstring = "pythonProgram"
stringslices = userstring[7:] + userstring [-1: 6]
print(stringslices)


# Check if a Substring is Present in a Given String
string1 = 'Python Programs'
string2 = 'Practice Python Programs'
if string2 in string1:
    print("yes")
else:
    print("no")

# using  find()


string1 = 'Python Programs'
string2 = 'Practice Python Programs'
result = string2.find(string1, 4)
if result == -1:
    print("result is not valid")
else:
    print(result)

# using regular expressions- re.search()

import re
string1 = 'Python Programs'
string2 = 'Practice Python Programs'
if re.search(string1, string2):
    print("The substring: {} is present in the given string: {}".format(string2, string1))
else:
    print("not present")


string = "I am learning python language. students should learn programing "
splitstring = string.split()
for item in splitstring:
    if len(item) %2 == 0:
        print(item)


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


import re
str1 = 'Python'
str2 = 'pythonProgram'
count = 0
for item in str1:
       if re.search(item, str2 ):
           count = count + 1
print("The count is: ", count)

