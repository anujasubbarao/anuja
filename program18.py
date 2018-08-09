n=int(raw_input())
l = 100
u = 100000

for num in range(l, u + 1):
   order = len(str(n))
   sum = 0
   temp = n
   while temp > 0:
       digit = temp % 10
       sum += digit ** order
       temp //= 10

   if num == sum:
       print(num)
