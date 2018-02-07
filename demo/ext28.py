# map/reduce

from functools import reduce

def add(x,y):
	return x+y

print(reduce(add,[1,2,3,4,5]))


def fun(x,y):
	return x*10 + y

print(reduce(fun,[1,2,3,4,5]))
