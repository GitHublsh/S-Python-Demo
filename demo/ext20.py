# 生成器
# 在Python中，这种一边循环一边计算的机制，称为生成器：generator。

L = [x*x for x in range(10)]

print(L)
for x in L:
	print(x)

g = (x*x for x in range(10))
next(g)
