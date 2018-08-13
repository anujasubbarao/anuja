def median(list):
    n = len(list)
    if n < 1:
            return None
    if n % 2 == 1:
            return list[n//2]
    else:
            return sum((list[n//2-1:n//2+1]))/2.0
            
number=int(raw_input())
list=[int(x) for x in raw_input().split()]
list.sort()
print median(list)
