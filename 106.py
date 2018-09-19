n,m=map(int,raw_input().split())
list=[int(x) for x in raw_input().split()]
count=0
for i in list:
	if i%2!=0:
		count=count+1
		count+=m
		print count
		break
