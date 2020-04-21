# Sum of squares of first n natural numbers
def firstsum(num):
    total = 0
    for val in range(1, (num+1)):
        total = total + (val **2)
    print("The sum of square: ", total)
num = int(input("Please enter your natural number: "))
firstsum(num)
