# 迭代器练习

it = iter([1,2,3,4,5])

while True:
	try:
		x = next(it)
		print(x)
	except StopIteration:
		break
