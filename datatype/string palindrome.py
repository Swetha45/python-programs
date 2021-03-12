
"""
if (s == s[::-1]):
    print("The nu is palindrome")
else:
    print("The nu is not palindrome")
"""
s = input("please enter a string: ")

c=reversed(s)
if list(c)==list(s):
    print("The number is palindrome")
else:
    print("The number is not palindrome")

