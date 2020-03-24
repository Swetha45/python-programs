"""n=int(int(input("please enter a integer number: ")))
if n%2==0:
    print("The number is Even")
else:
    print("The number is odd")"""

num = int(input("give me a number to check: "))
check = int(input("give me a number to divide by: "))
if num%2==0:
    print(num,  "is the even")
else:
    print(num, "is the odd")

if num%check==0:
    print(num, " is divisable by", check)
else:
    print(num, " is not divisable by", check)
