n=int(raw_input())
temp = n
rev=o
while(n>0):
      rem=n%10
      rev=rev*10+rem
      n=n//10
 if(temp==rev):
         print("Yes")
 else:
         print("No")
