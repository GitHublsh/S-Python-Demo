# 高阶函数

def add(x,y,f):
	return f(x) + f(y)

print(add(-1,1,abs))
