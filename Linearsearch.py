list = [-100, 8, 20, 0.196, 3, 6]
key = 6
for x in range(len(list)):
    if key == list[x]:
        print("The key {} is present in the list. The original list is: ".format(key), list)
        break
else:
    print("Key {} is not present in the list". format(key))