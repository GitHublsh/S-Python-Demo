def nop():
	pass


def my_abs(x):
	if x>=0:
		return nop()
	else:
		return -x

s = my_abs(12)

print(s)

s = my_abs(-1)

print(s)





