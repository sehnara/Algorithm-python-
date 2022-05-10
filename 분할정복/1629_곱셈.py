# 14:11 ~  [메모리 초과] 메모리 초과는 어떻게 분석해보면 되지?
A, B, C = map(int, input().split())
dp = [0] *(B+1)
dp[1] = (A) % C
dp[2] = (A*A) % C
for i in range(3,B+1):        
    dp[i] = (dp[i-1] * dp[1]) % C
        
    if i == (B//2):
        if B % 2 == 1:
            print(dp[i] * dp[i] * A % C)
        else :
            print(dp[i] * dp[i] % C)
# print(dp)


