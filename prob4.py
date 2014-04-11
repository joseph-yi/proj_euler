#prob 4
hehe=[]
for i in range(100,1000):
	for j in range(i,1000):
		h=str(i*j)
		if h==h[::-1]:
			h=int(h);
			hehe.append(h)
			

print max(hehe)