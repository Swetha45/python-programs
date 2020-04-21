def selectionsort(number):
    for ele in range (0, len(number)):
        min_value = min(number[ele:])
        min_index = number.index(min_value)
        # use swap method-------> number[ele], number[min_index] = number[min_index], number[ele]
        # or use temp variable
        temp = number[ele]
        number[ele] = number[min_index]
        number[min_index] = temp
number = [-61, 64, 25, 0.15, 12, 0, 22, 11, -10]
selectionsort(number)
print(number)