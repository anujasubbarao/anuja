n=int(raw_input())
def test_prime(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,1000):
            if(n % x==0):
                return False
        return True             
print(test_prime(7))


