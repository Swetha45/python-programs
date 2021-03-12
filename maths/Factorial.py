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


