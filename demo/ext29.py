# map
# 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。

from functools import reduce

def normalize(name):
	return name.title() 
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# list求和
def add(x,y):
	return x*y

def prod(L):
	return reduce(add,L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')


# str2float

def str2float(s):
	return float(s)

print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
