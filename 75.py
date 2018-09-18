str=raw_input()
l=len(str)
strl=list(str)
k=int(round((l//2)))
if(l%2==0):
	str1[k]='*'
	strl[k-1]='*'
else:
	strl[k]='*'
ans=''
for i in strl:
         ans=ans+i
print ans
