import numpy as np
with open('prob13.txt') as f:
    content = f.readlines()
    
g = np.array(content)
#g is now a length 100 array of strings 0:49 is the string, 50 --> \n
#digits = []
def solver(array):
    remains = 0
    digits=[]
    for i in xrange(49,-1,-1):
        #loop for each digit
        num = 0
        #print remains
        for j in xrange(100):
            #loop for each row
            try:
                number=int(float(g[j][i]))
                num += number
            except ValueError:
                print g[j][i]
                print i,j
                raw = raw_input()
        
        if i > 0 :    
            digits+=[(num+remains) % 10]
            remains = (num+remains) / 10
        else:
            digits+= [num+remains]
    return digits
    
x = solver(g)
x=x[::-1]

#5537376230