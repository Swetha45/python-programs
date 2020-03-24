import urllib
import re
name=input("Please enter your string here: ")
text= "?"
params=int(input("How many params you want: " ))
if params>=1:
    name=name+text
    for x in range(0, params):
        p1 = input("Enter your params name: ")
        name = name + p1 +"="
        p2 = input("Please enter pa values: ")
        name = name + p2
        if x != params-1:
            name = name + "&"
            print("The total params value is: ", params)
    print("Final string is: " + name)
else:
    print("The last string values is: " + name)


