N,k=map(int,raw_input().split())
list=[int(x) for x in raw_input().split()]
if N in list:
     count=list.count(N)
     print(count)
elif k in list:
     count =list.count(k)
     print (count)
else:
     print(0)
