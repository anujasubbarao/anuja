n=int(raw_input())
temp=n
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+dig
    n=n//10
if(temp==rev):
    print("The number is a palindrome")
else:
    print("The number isn't a palindrome")
