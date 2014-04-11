#find smallest number divisible by 1...20 EVENLY


#2,3,5,7,9,11,13,17,19 

import numpy as np

lst = xrange(11,21)
def problem():
	i= 0
	starting= 2*3*5*7*9*11*13*17*19
	
	#print starting
	while i==0:
		
		if all(starting %i ==0 for i in lst):
			h=starting/np.array(lst)
			if all(i%2==0 for i in h):
				i=1
				print starting
				return starting
			else:
				print starting
				starting+=2*3*5*7*9*11*13*17*19
		else:
			#print starting
			starting+=2*3*5*7*9*11*13*17*19
problem()            