s1 = "abcdefgh"
s2 = "hgfedcba"
if len(s1) == len(s2):
    isMirror = True
    for val in range(0, len(s2)):
        if s1[val] != s2[len(s2) - val - 1]:
            print("inside if")
            isMirror = False
            break
    if isMirror: print("mirror")
    else: print("not mirror")
else:
    print("The string lengths are not equal")