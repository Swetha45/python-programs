# take  a input from user
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

    userdecision = input("Do you want to continue/exit (cn/ex) : ")
    if userdecision == 'ex':
        exit()