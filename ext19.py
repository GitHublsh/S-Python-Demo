# 列表生成

# L = list(range(1,10))

# for x in L:
# 	print(x)


L = [x*x for x in range(1,11) if x % 2 == 0]

for x in L:
	print(x)

L1 = ['Hello','World',18,'Apple',None]

L2 = [x for x in L1 if isinstance(x,str)]

for y in L2:
	print(y)