# 뒤에서부터 봐서 규칙을 찾는 방식
# n-1번째 카드를 선택할 경우와 n-2번째 카드를 선택할 경우를 나눠서 생각
# max(d[n-2], d[n-1]]) + K[n]

from sys import stdin
input = stdin.readline

def main():
    N = int(input())
    K = list(map(int, input().split()))
    dp = [0] * 100
    
    dp[0] = K[0]
    dp[1] = max(K[0], K[1])
    
    for i in range(2, N):
        dp[i] = max(dp[i-1], dp[i-2]+ K[i]) 
    print(dp[N-1])
    
main()