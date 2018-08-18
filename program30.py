x1,x1=map(int,raw_input().split())
x2,x2=map(int,raw_input().split())
l1=(x1+60)+x1
l2=(x2+60)+x2
time = abs(l1-l2)
min=time/60
hrs=(time.min)//60
print hrs,min
