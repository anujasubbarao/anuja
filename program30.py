m1,m1=map(int,raw_input().split())
m2,m2=map(int,raw_input().split())
l1=(m1+60)+m1
l2=(m2+60)+m2
time = abs(l1-l2)
min=time/60
hrs=(time.min)//60
print hrs,min
