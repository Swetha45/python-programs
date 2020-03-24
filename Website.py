import urllib
import re
url = input("Please enter your base url: ")
paramCount = int(input("How many params you want add to url: " ))
if paramCount >= 1:
    url = url + "?"
    for count in range(0, paramCount):
        p1 = input("Enter your params name: ")
        url = url + p1 + "="
        p2 = input("Please enter pa values: ")
        url = url + p2
        if count != paramCount - 1:
            url = url + "&"
    print("Parameterized URL string: " + url)
else:
    print("Parameterized URL string: " + url)


