# 11:03 ~ 11:23
# dp 배열의 앞뒤 관계를 확인하면서 
N = int(input())
dp = [0] * 1000001
dp[1] = 1
dp[2] = 2
for i in range(3,N+1):
    dp[i] = (dp[i-2] + dp[i-1])% 15746
   

print(dp[N])