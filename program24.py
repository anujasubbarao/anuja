number=int(raw_input())
list=[]
for i in range(0,number):
    newNo=int(input(''))
    a=list.append(newNo)
list.sort()

print " ".join(map(str,list))
