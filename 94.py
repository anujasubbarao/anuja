s1,s2=map(str,raw_input().split())
list=[int(x) for x in raw_input().split()]
if s1==s2:
	print s1
elif len(s1)>len(s2):
	print s1
else:
	print s2
		
