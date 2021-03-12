import sys
p1=input("player1 name ? ")
p2=input("player2 name ?")
#r1=input("do yo want to choose rock, paper or scissors?", u1)
u1 = input("%s, do yo want to choose rock, paper or scissors?")
u2 = input("%s, do you want to choose rock, paper or scissors?")
def com(u1,u2):
    if (u1==u2):
        return ("Its tie")
    elif u1== 'rock':
        if u2== 'scissors':
         return ("rock wins")
        else:
         return ("scissors wins")
    elif u1== 'scissors':
        if u2=='paper':
            return("scissors wins")
        else:
            return ("paper wins")
    elif u1=='paper':
        if u2=='rock':
            return ("paper wins")
        else:
            return ("rock wins")
    else:
        return("Please select one from the rock, paper or scissors?")
print(com(u1,u2))




