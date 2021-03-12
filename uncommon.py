def uncommon(u1, u2):
    thirdlist = " "
    for first in u2.split():
        if first not in u1.split():
            thirdlist = thirdlist + " " + first
        elif first not in u2.split():
            thirdlist = thirdlist + " " + first
    print(thirdlist)

u1 = "talent book pen mouse computer"
u2 = "animal human car book pen computer laptop"
uncommon(u1, u2)