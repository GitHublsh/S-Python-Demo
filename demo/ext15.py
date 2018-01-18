import math

def move(x,y,step,angle = 0):
	nx = x+step*math.cos(angle)
	ny = y-step*math.sin(angle)
	return nx,ny

def power(x):
	return x*x

print(power(2))

def enroll(name, gender):
    print('name:', name)
    print('gender:', gender)

enroll('Hello',"f")

d = {'a':1,'b':2,'c':3}
for key in d:
	print(key)

for ch in 'ABC':
	print(ch)