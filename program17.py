n=int(raw_input())
sum = 0
times = 0
temp = n
while temp > 0:
        times = times + 1
        temp =  10
temp = n
while temp > 0:
        rem = temp %10
        sum = sum+ (Rem ** times)
        temp =10
if n== sum:
        print("Yes")
else:
        print("No")

