import urllib
import re

url = input("Please enter base url: ")
paramCount = int(input("How many params you want in url: "))
if paramCount >= 1:
    url = url + "?"
    for count in range(0, paramCount):
        p1 = input("Enter your param name: ")
        url = url + p1 + "="
        p2 = input("Enter value for param: ")
        url = url + p2
        if count != paramCount - 1:
            url = url + "&"
    print("Parameterized URL string is: " + url)
else:
    print("Parameterized URL string is: " + url)
