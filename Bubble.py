# Bubble sort
def mybubble(mylist):
    emptylist = []
    for val in range(0, mylist):
        user = int(input("Enter element: "))
        emptylist.append(user)
        for i in range(0, len(emptylist)):
            for j in range(len(emptylist)-1):
                if emptylist[j] > emptylist[j+1]:
                    #swap the elements
                    emptylist[j], emptylist[j+1] = emptylist[j+1], emptylist[j]
    print(emptylist)
mylist= int(input("How many number of elements you want: "))
mybubble(mylist)

