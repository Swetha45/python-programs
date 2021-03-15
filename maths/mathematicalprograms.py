# 1Q: Print ASCII Value of a character
# we use the ord() to convert the character into the ASCII
character = 'P'

if character.isnumeric():
    print("You entered number. Please enter the character")
else:
    print("The above character ASCII value is", ord(character))

#2Q: Python Program for Sum of squares of first n natural numbers

     #Natural no start with 1

def naturalnumber(number):
    square = 0
    if number <= 0:
        print("The number is not natural number")
    else:
        for values in range(1, number+1):
                square = square + (values * values)
        print(square)
        return square

number = int(input("Please enter natural number : "))
naturalnumber(number)

# 3Q: Python Program for cube sum of first n natural numbers

number = 4
cube = 0
if number <= 0:
    print( "The number is not natural number" )
else:
    for values in range(1, number+1):
        cube = cube + (values * values * values )
    print("The cube sum of first n natural numbers are" , end = '\n' "result: {}".format(cube) )

# 4Q: Take a input from user for basic calculator
def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

isContinue = True
while isContinue:
    firstnumber = int(input("please enter your first number: "))
    secondnumber = int(input("please enter your second number: "))
    inputuser = input("please select your operator: ")
    if inputuser == '+':
            result = addition(firstnumber, secondnumber)
    elif inputuser == '-':
            result = subtraction(firstnumber, secondnumber)
    elif inputuser == '*':
            result = multiplication(firstnumber, secondnumber)
    elif inputuser == '/':
            result = division(firstnumber, secondnumber)
    print("The result is: {}".format(result))

    userdecision = input("Do you want to continue (yes/no)? : ")
    if userdecision == 'no':
        exit()

# 5Q: Find the factorial of number

    # using for loop
def factorial(n):
    fact = 1
    if n < 0:
        print("We can not do the factorial to negative numbers")
    elif n == 0:
        print("The factorial of 0 is 1")
    else:
        for x in range( 1, n + 1 ):
            fact = fact * x
        print(fact)

n = 4
factorial( n )

# using while loop

Number = int(input("please enter a factorial number: "))
fact = 1
if Number <= 0:
    print("Please enter a number other than 0 and negative numbers")
else:
    while Number > 0:
        fact = fact * Number
        Number -= 1
    print("The Factoral of the given number is {}".format(fact))

# 6Q: Print prime numbers between 1 to 10

number = int(input("Please enter your prime number :"))
if number > 1:
    for value in range(2, number):
        if (number % value == 0):
            print( "The {} is not a prime number".format( number ) )
            break
    else:
        print("The number is prime", number )
else:
    print("Prime numbers starts from 2", end = '\n' "Please enter another number")


# 7Q:  Find simple Interest
#  si = p * T * /100

def interest(Value1, Value2, Value3):
    si = (Value1 * Value2 * Value3)/100
    print("The simple interest of above numbers", si)
    return si
Principal = int( input( "Please enter your principal amount :" ) )
Time = int( input( "Please enter your time:" ) )
Rate = int( input( "Please enter your rate:" ) )
interest( Principal, Time, Rate )

# 8Q: How to find Compound Interest

# A = P(1 + R/100) t
# Compound Interest = A – P

def compoundinterest(principal,rate,time):
    amount = principal * (pow((1+ rate / 100),time))
    print( "The total amount is", amount )
    ci = amount - principal
    print("The compound interest is:", ci)
compoundinterest( 10, 20, 30 )


# 9Q:


