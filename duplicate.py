# find the first duplicate word, example string: “this is just a wonder, wonder why I have this in mind”
Mystring = 'This is just a wonder wonder why I have this in mind'
print("The actual sting is:", Mystring)
Duplicatelist = []
Count = 0
for Word in Mystring.split():
    if Word in Duplicatelist:
        Count += 1
        print("The duplicate word is : '{}'. Appeared {} time(s) in a given string". format(Word, Count))
    elif Word not in Duplicatelist:
        Duplicatelist.append(Word)
print("After removing the duplicates. The final string is", Duplicatelist)