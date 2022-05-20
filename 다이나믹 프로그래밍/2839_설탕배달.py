def main():
    N = int(input())
    dp = [5001] *(5001)
    dp[3] = 1
    dp[5] = 1
    for i in range(5,N+1):
        dp[i] = min(dp[i-3] +1 , dp[i])
        dp[i] = min(dp[i-5] +1, dp[i])
    
    if dp[N] == 5001 :
        print(-1)
    else :
        print(dp[N])    
main()