str=raw_input()
l=len(str)
str1=list(str)
k=int(round((l//2)))
if(l%2==0):
	str1[k]='*'
	str1[k-1]='*'
else:
	str1[k]='*'
ans=''
for i in str1:
         ans=ans+i
print ans
