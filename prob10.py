#problem 10

from math import sqrt
def primes_less(x):
    y=range(1,x,2)
    y.remove(1)
    y=[2]+y
    sieve_list = range(3,sqrt(x),2)
    for every_number in y:
        up_to_max = range(3,x/every_number,2)
        for z in up_to_max:
            try:
                y.remove(z*every_number)
            except ValueError:
                pass
    return y
                
    
    
def sieve(n):
    np1 = n + 1
    s = range(np1) #this is my y
    s[1]=0
    sqrtn=int(round(n**0.5))
    for i in xrange(2,sqrtn+1): #this is my sievelist
        if s[i]:
            s[i*i:np1:i] = [0]*len(xrange(i*i,np1,i))
    return filter(None,s)
        












            