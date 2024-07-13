def min_max(ls):
    min =ls[0]
    max = ls[0]
    for element in ls:
        if element<min:
            min = element
        if element>max:
            max = element

    return min, max
mymin, mymax = min_max([100,1,5,60,6,7, 2])
print(mymin, mymax)