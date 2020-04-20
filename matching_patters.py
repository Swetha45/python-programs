Firststring = '-/@swejkk%&$32^@$$$'
Secondstring = 's/r34k%@'
# use the set method to remove duplicated from the string
Set1 = set(Firststring)
Set2 = set(Secondstring)
# use the intersection() to get a common values form both sets
Inter= Set1.intersection(Set2)
print("Number of matching characters in a pair of string: ", len(Inter))
# use the union() to get a all values form both sets. other than duplicates
Uni = Set1.union(Set2)
print("Number of characters from both sets: ", len(Uni))
Sup = Set1.issuperset(Set2)
print("Set1 issuperset of set2:",  Sup)
Sub = Set2.issubset(Set1)
print("Set2 issubset of set1:", Sub)