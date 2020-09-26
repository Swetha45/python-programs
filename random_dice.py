import random
class RandomDice:
    def __init__(self):
            self.lowestNumber = 1
            self.highestnumber = 6
            diceoption = int(input("How many dices you want: "))
            roll_dice = "yes"
            while roll_dice == 'yes':
                for option in range(1, diceoption+1):
                    self.dice1()
                roll_dice = input("Do you want to roll the dice: yes/no --")
    def dice1(self):
        print(random.randint(self.lowestNumber, self.highestnumber))
RandomDice()
