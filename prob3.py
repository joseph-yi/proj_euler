#prob3
"""
import numpy as np
from math import floor
def primer(x):
	i=2
	while i<x/2:
		
		if np.mod(x,i)==0:
			print(i)
		i+=1
primer(600851475143);
"""
from math import sqrt
primes = set([2])
value = 3
number = 317584931803
while value < sqrt(number):
    isPrime = True
    for k in primes:
        if value % k == 0:
            isPrime = False
            value += 2
    if isPrime:
        primes.add(value)
        if number % value == 0:
            print value
            number /= value
print number