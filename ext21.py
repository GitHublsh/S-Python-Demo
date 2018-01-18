# 打印杨辉三角

def yanghui(x):
	if x==0:
		return 0
	if x==1:
		return 1
	if x>1:
		return yanghui(x-1)+yanghui(x-2)


print(yanghui(3))