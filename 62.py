n=raw_input()
count =0
for i in n:
      if((i=='0') or (i=='1')):
      	           count+=1
if (count==(len(n))):
	print("yes")
else:
	print("no")
