n=int(raw_input())
l=[int(x) for x in raw_input().split()] 
for i in range(1,n):
    if l.count(i)==1:  
    	print i
