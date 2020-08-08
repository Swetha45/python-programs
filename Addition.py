
# addition of two numbers

a= 20.5
b= 30.5
c = a + b
print("The addition of two numbers are",  c)


# user input
def addition(Value1, Value2):
    if Value1.isdigit() and Value2.isdigit():
        print( "The Addition of {0} and {1} is {2}".format( Value1, Value2, Value3 ) )
        print( "The given value is integer:", isinstance( Value3, int ) )
    else:
        print("The given value is not an integer")
Value1 = input("Please enter your first number : ")
Value2 = input("Please enter your second number " )
Value3 = int( Value1 ) + int( Value2 )
addition(Value1, Value2)
print("The type of user input is", type(Value3))