# 迭代器
from collections import Iterable
print(isinstance('abc',Iterable))

print(isinstance([1,2,3],Iterable))

print(isinstance(123,Iterable))

for x,y in [(1,2),(3,4),(5,6)]:
	print(x,y)
