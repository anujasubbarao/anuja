t=int(raw_input())
l=[int(x) for x in raw_input().split()] 
for i in range(1,t-1):
    if l.count(i)==2:  
    	print i,
