# # 1 Sort Python Dictionaries by Key or Value
# method 1-- sorted dict
dictionary = {'name': 455, 'age': 20, 'education' : 12}
for value in sorted(dictionary.keys()):
    print("The keys are:", value)
for key in sorted(dictionary):
    print((key, dictionary[key]), end = " ")

# method 2 -- OrderedDict
from collections import OrderedDict

dictionary = {'name': 'xxx', 'age': '19', 'education': 'bachelor'}
dict1 = OrderedDict(sorted(dictionary.items()))
print(dict1)

# 2 Handling missing keys in Python dictionaries

#Method  get(key, defaultvalue)
#
def missingkeys(dictionary):
    getmethod = dictionary.get('age', 'value not found')
    getvalue = dictionary.get('ageee', 'value not found')
    print("If key is present result : ", getmethod)
    print("If keys is not found then : ", getvalue)
dictionary = {'name': 'xxx', 'age': '19', 'education': 'bachelor'}
missingkeys(dictionary)

# setdefault() Method

def missingkeys(dictionary):
    print("the original dictioanry is : ", dictionary)
    setmethod = dictionary.setdefault('age', 'value not found')
    setvalue = dictionary.setdefault('ageee', 'value not found')
    print("If key is present then the value is : ", setmethod)
    print("If keys is not found then : ", setvalue)
dictionary = {'name': 'xxx', 'age': '19', 'education': 'bachelor'}
missingkeys(dictionary)
print("After changes the dictionary is: ", dictionary)

# defaultdict method
import collections
countrydict = collections.defaultdict(lambda : 'key not found')
#countrydict = {"India": "IN", 'USA': 'US', 'Canada': 'can'}
countrydict['india'] = 'in'
countrydict['USA'] = 'ua'
print(countrydict["india"])
print(countrydict['ll'])

# sigle key hild a multiple values

colorsdict = {'green' : ('gr', 'g', 'light green'),
              'yellow': ('ye', 'y', 'light yellow'),
              'pink' : ('pk', 'p', 'light pink')
              }
print("The value index of green key is: ", colorsdict['green'][0])
print("The value index of yellow key is: ", colorsdict['yellow'][1])
print("The value index of pink key is: ", colorsdict['pink'][2])


# find the sum of all items in a dictionary
numbersdict = {'key1': 5, 'key2':10, 'key3':15, 'key4' : 20}
sum = 0
result = 0
for item in numbersdict:
    sum = sum + numbersdict[item]
print("The sum of all items in dictioanry:", sum)
# or use the values to grab all the values from the keys
for val in numbersdict.values():
    result = result + val
print("The result is: ", result )


# Ways to remove a key from dictionary

numbersdictt = {'key1': 5, 'key2':10, 'key3':15, 'key4' : 20}
del numbersdictt['key1']
numbersdictt.pop('key3')
numbersdictt.popitem()
# remove all items
numbersdictt.clear()
print("After removing a key result : ", numbersdictt)

# Merging two Dictionaries
#1. update
dictionary1 = {'key1': 5, 'key2':10, 'key3':15, 'key4' : 20}
dictionary2 = {'key5': 90, 'key7' : 100}
dictionary2.update(dictionary1)
print(dictionary2)

# 2. **
dictionary1 = {'key1': 5, 'key2':10, 'key3':15, 'key4' : 20}
dictionary2 = {'key5': 90, 'key7' : 100}
dictionary3 = {**dictionary2, **dictionary1}
print(dictionary3)

# Convert a list of Tuples into Dictionary
# method 1 : setdefault

dictionary1 = [("A", 10), ("B", 20), ("c", 30)]
dictionary2 = dict(())
for key, value in dictionary1:
    result = dictionary2.setdefault(key, [])
    result.append(value)
print(dictionary2)

 # method 2 -- dict()

dictionary1 = [("A", 10), ("B", 20), ("c", 30)]
print(dict(dictionary1))


# Find all duplicate characters in string

# use Counter()

from collections import Counter
namestring ="duppcharrss"
countermethod = Counter(namestring)
for key, value in countermethod.items():
    if value > 1:
        print(key, end = " ")


# 11. Find common elements in three sorted arrays by dictionary intersection

from collections import Counter
ar1 = [1, 50, -12, 90, 67, 89]
ar2 = [6, 1, 50, 89, -12, 963  ]
ar3 = [3, 4, 23, 29, -12, 90, 1]

dict1 = dict(Counter(ar1))
dict2 = dict(Counter(ar2))
dict3 = dict(Counter(ar3))
intersection = (dict1.items() & dict2.items() & dict3.items())
for key, value in intersection:
    print(key, end = " ")

# Python counter and dictionary intersection example (Make a string using deletion and rearrangement)

from collections import Counter
string1 = 'AAABBBCCC'
string2= 'AAABBBCCCDHFJFKGLGL'
counter1 = Counter(string1)
counter2 = Counter(string2)
intersetions = counter1 & counter2
if intersetions == counter1:
    print("Possible to Rearrange")
else:
    print("Not Possible to Rearrange")


# Remove all duplicates words from a given sentence
from  collections import Counter
string = "Geeks for Geeks"
split1 = string.split(" ")
for i in range(0, len(split1)):
        split1[i] = "".join(split1[i])
#joinstring = "".join(split1)
counter1 = Counter(split1)
s = "".join(counter1.keys())
print(s)


