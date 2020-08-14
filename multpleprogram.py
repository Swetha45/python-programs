#print ASCII Value of a character
# we use the ord() to convert the character into the ASCII

character = 'P'

if character.isnumeric():
    print("You entered number. Please enter the character")
else:
    print("The above character ASCII value is", ord(character))


# Python Program for Sum of squares of first n natural numbers

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


#Python Program for cube sum of first n natural numbers

number = 4
cube = 0
if number <= 0:
    print( "The number is not natural number" )
else:
    for values in range(1, number+1):
        cube = cube + (values * values * values )
    print("The cube sum of first n natural numbers are" , end = '\n' "result: {}".format(cube) )


