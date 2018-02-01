# 高阶函数 

# 求绝对值

print(abs(-3))

x = abs(-12)

print(x)

def function(x):
	return abs(x)

print(function(-1))

def add(x,y,f):
	return f(x)+f(y)

print(add(-1,-2,abs))

