# 뒤에 붙을 카드를 가지고 앞의 dp 구상

from sys import stdin
input = stdin.readline

N = int(input())
dp=[0] * 1001
dp[1] = 1
dp[2] = 3

for i in range(3,N+1):
    dp[i] = dp[N-1] + (dp[N-2] * 2)
    
print(dp[N])