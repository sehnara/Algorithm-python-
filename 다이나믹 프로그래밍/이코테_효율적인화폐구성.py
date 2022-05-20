from sys import stdin
input = stdin.readline

def main():
    N, M = map(int, input().split())
    MONEY = [int(input()) for _ in range(N)]
    dp = [10001] * (M+1) # ------------------------------------
    dp[0] = 0
    for i in range(1,M+1):
        for m in MONEY:            
            dp[i]= min(dp[i], 1 + dp[i-m]) #--------------------------------
    
    if dp[M] == 10001 :
        print(-1)
    else :
        print(dp[M])
    
main()