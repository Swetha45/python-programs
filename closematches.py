# # Python program to find uncommon words from two Strings
# def uncommon(u1, u2):
#
#         firstcount = 0
#         secondcount = 0
#         newfirstlist= []
#         newsecondlist = []
#
# # split the every word in the u1 and u2. use two for loops
#         for first in u1.split():
#                 if first not in newfirstlist:
#                         newfirstlist.append(first)
#                 else:
#                      firstcount = firstcount + 1
#                      print("Common letters from first string is: ", {first})
#         for second in u2.split():
#                 if second not in newsecondlist:
#                         newsecondlist.append(second)
#                 else:
#                      secondcount = secondcount + 1
#                      print("Common letters from second string is: ", {second})
#         print("Uncommon words from the first list is: ", newfirstlist)
#
#         print("The total repeated words from first list is: ", firstcount)
#
#         print("Uncommon words from the second list is: ", newsecondlist)
#
#         print("The total repeated words from second list is: ", secondcount)
#
#
# u1 = "she is student and she is teacher"
# u2= "string repeats string times"
# uncommon(u1, u2)
