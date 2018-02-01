# 迭代器

# 通过isInstance 判断是否为迭代器

from collections import Iterable

isinstance({},Iterable)

print(isinstance({},Iterable))

print(isinstance([],Iterable))

print(isinstance((),Iterable))

print(isinstance(100,Iterable))
