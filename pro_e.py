#project euler codes

#sum of fibonacci
import numpy as np
from math import sqrt
def fib(n):
	return int((((1.0+sqrt(5))/(2))**n-\
			((1.0-sqrt(5))/(2))**n)/(sqrt(5)))
			
	
x=1
i=0
while x==1:
	if fib(i)<4000000:
		i+=1
	if fib(i)>=4000000:
		print(i)
		x=0
summer = range(i)
for z in summer:
	summer[z] = fib(z)
print(summer)
summer = np.array(summer)



T= 0
for q in summer:
	if q%2==0:
		T+=q
print(T)