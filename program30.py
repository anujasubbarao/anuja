n1,n1=map(int,raw_input().split())
n2,n2=map(int,raw_input().split())
i1=(n1+60)+n1
i2=(n2+60)+n2
time = abs(i1-i2)
min=time/60
hrs=(time.min)//60
print hrs,min
