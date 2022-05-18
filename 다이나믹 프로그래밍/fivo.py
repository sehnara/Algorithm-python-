# 피보나치 수열
# 1단계
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x-2) + fibo(x-1)

# 2단계
d = [0]*100

def fibo2(x):
    if x == 1 or x ==2 : 
        return 1
    
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo2(x-1) + fibo2(x-2)
    return d[x]
print(fibo2(8))

# 3단계
d = [0] * 100
d[1] = 1
d[2] =1
n= 99

for i in range(3, 99):
    d[n] = d[n-1] + d[n-2]