def main():
    N = int(input())
    dp = [0] * (N+1)
    dp[1] = 1
    m = 1000000
    p = 15 * 10**(m//10 -1) 
    
    for i in range(2, 2 + p):
        dp[i] = (dp[i-1] + dp[i-2]) % m
    
    print(dp[N % p])
main()