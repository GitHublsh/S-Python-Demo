# sorted 排序

from operator import itemgetter


L1 = [1,3,2,4,5,8,6]

print(sorted(L1))

# 可自定义排序,可接受一个key函数来实现

L2 = [1,2,-4,3,8,-9]

print(sorted(L2,key = abs))

# 忽略大小写比较字符串

L3 = ['An','Dan','co','El','ban']

print(sorted(L3,key = str.lower))

# 反向排序

print(sorted(L1,reverse = True))

# tuple 排序
L4 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

# 按名字排序

print(sorted(L4,key = itemgetter(0)))

# 按成绩排名

print(sorted(L4,key = itemgetter(1)))

# 成绩从高到低

print(sorted(L4,key = itemgetter(1),reverse = True ))


