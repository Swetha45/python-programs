Guess = int(input("Please guess the correct number from 1 to 100: "))
while Guess <= 100:
    print("OOPS!, Please check your number")
    Guess = int(input("Please guess the correct number from 1 to 100 : "))

print("You win ! {} is vaild number: ".format(Guess))

