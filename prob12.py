import math
import numpy as np
def sieve(n):
    np1 = n + 1
    s = range(np1) #this is my y
    s[1]=0
    sqrtn=int(round(n**0.5))
    for i in xrange(2,sqrtn+1): #this is my sievelist
        if s[i]:
            s[i*i:np1:i] = [0]*len(xrange(i*i,np1,i))
    return filter(None,s)
        
def triangles(number, range_start=2):
    if range_start == 2:
        start = 1
    if range_start != 2:
        start = sum(range(range_start))
    
    assert number>2
    for i in xrange(range_start,number):
        prime_list = sieve(i+1)
        start += i
        #print start
        h = map(lambda x: start%x ==0,prime_list)   
        l =filter(lambda z: z==True, h)
        #add to len(l) the powers
        l = len(l)
        h = np.array(h)
        if h.size>1:
            pl_array = np.array(prime_list)
            prime_dividers = pl_array[h==1] 
            mults=check_powers(start,prime_dividers)
            m_prods = reduce(lambda x,y:x*y, mults)
        else:
            mults = []
            m_prods = 2**l
        if m_prods  >= 500:
            print "Answer is found! \n"
            print m_prods, "\n"
            
            
            return start,m_prods,mults, prime_dividers, i
    #ANSWER: triangular number
    #l = number of unique prime divisors
    #m = number of divisors 
    return "boo"

    
    
    
    
def check_powers(number,dividers):
    
    if type(dividers) != int:
        result = []
        for divs in dividers:
            j = 2
            while True:
                if number % (divs)**j != 0:
                    result +=[j]
                    break
                j+=1
        assert len(result) == len(result)
        return result
        
    else:
        
        j = 2
        while True:
            if number% (dividers)**j != 0:
                return [j]
            j+=1
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    