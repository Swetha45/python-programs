"""a= [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
b=[]
for i in a:
    if i%2==0:
        b.append(i)
print("The list contains the only even numbers", b)"""

def ran(x):
    b = []
    for i in x:
        if i % 2 == 0:
            b.append(i)
    print("The list contains  only even numbers", b)
x= [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
ran(x)