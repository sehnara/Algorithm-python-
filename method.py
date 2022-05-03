# 1. 소수 판별(에라토스테네스의 체)
def is_prime(n) :
    arr = [True] * (n+1);
    arr[0] = False;
    arr[1] = False;
    
    for i in range(2,n+1):
        if arr[i] == True:
            j = 2;
            
            while (i*j) <= n:
                arr[i*j] = False;
                j += 1;
    return arr;