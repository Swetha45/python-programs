# take the prime numbers between 1 to 10

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