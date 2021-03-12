import program

n=program.randint(1, 9)

while gu!=n and gu!='exit':
    gu =input("please enter any number from 1 to 9: ")
    if gu == "exit":
        break
    gu=int(gu)
    count +=1

    if gu<n:
            print("The number is low")
    elif gu>n:
            print("The number is high")
"""
import  random

number = random.randint(1, 9)
guess = 0
count = 0

while guess != number and guess != "exit":
    guess = input("What's your guess?")

    if guess == "exit":
        break

    guess = int(guess)
    count += 1

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print("You got it!")
        print("And it only took you", count, "tries!")"""

