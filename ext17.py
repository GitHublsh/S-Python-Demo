# 查找最大和最小值test
from collections import Iterable
def findMinAndMax(L):

    if not isinstance(L, Iterable):
        return (None, None)

    min=max=L[0]

    for value in L:
        if value < min:
            min = value
        if value > max:
            max = value

    return (min, max)


i = findMinAndMax([0,3,2,5,1])

print(i)