#  step 1: import module
import operator
# step 2 : read file
Fileopen = open("readfile.txt", "r")
Readfile= Fileopen.read().lower()
# Step 3: close the file
Fileopen.close()
# step 4: create empty dic
Words = {}
# step 5: split words in the file and count the key, value pairs
for x in Readfile.split():
    if x in Words:
        Words[x] += 1
    else:
        Words[x] = 1
# step 6:  sort the file
Sortedvalues = sorted(Words.items(), key=operator.itemgetter(1), reverse=True)
print(Sortedvalues)
# step 7:  create new file and open
Newfile = open ("read-count.txt", "w")
# step 9:  retrieve  duplicate and unique words from list
Newfile.write("The total words in file: {} \nThe unique words in file: {} \n" . format(len(Readfile.split()), len(Sortedvalues)))
# step 8:  retrieve items in key, value pair
for word in Sortedvalues:
    Newfile.write("{1} - {0}\n".format(word[1], word[0]))
Newfile.close()