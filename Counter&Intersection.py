from collections import Counter
str1 =  set("fgx123")     #[234, 4567, -452, 90.889]    #'1238785kjkjk-2'
str2 =  set("90xgf231")    #[8752, 9633, 234, 789]        #'3454adsf*963'
# convert the strings into the dictionary. using Counter()
c1 = Counter(str1)
c2 = Counter(str2)
inter = c2 & c1
if inter == c1:
    print("Possible to convert into string. The result is :", inter)
else:
    print("not possible")