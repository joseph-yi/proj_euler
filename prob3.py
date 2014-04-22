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
#set is a non-indexed set. because of this, it is MUCH faster than making a list or a tuple
value = 3 #the first prime number we start with (since we know the number is not even)
number = 600851475143
while value < sqrt(number): #up to sqrt since that is the largest possible divisor of number
    isPrime = True
    #default: 
    for k in primes:
        #for every number in our PRIME NUMBER set --> if value is divisible, then the VALUE
        #is NOT prime --> 
        #the consequence is that we will check the next odd number (the +=2)
        #the (if isPrime) will not be executed if not prime
        if value % k == 0:
            isPrime = False
            value += 2
    if isPrime:
        #first, since the value is prime, we want to add it to our set.
        primes.add(value)
        
        if number % value == 0:
            #value divides, so print value
            print value
            number /= value
print number

