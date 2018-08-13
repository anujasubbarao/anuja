def median(list):
    n = len(list)
    if n < 1:
            return None
    if n % 2 == 1:
            return list[n//2]
    else:
            return sum((list[n//2-1:n//2+1]))/2.0
            
number=int(raw_input())
list=[]
for i in range(0,number):
    newNo=int(input( ))
    a=list.append(newNo)
list.sort()
print median(list)
