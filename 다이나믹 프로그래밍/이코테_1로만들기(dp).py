from sys import stdin
input = stdin.readline

def main():
    X = int(input())
    dp = [0] * 30001 # 1~26까지의 모든 수가 어떤 연산을 거쳐 1이 될 때까지 연산 횟수를 각 저장
    
    for i in range(2,X+1):
        dp[i] = dp[i-1] + 1 # -1 했을 때의 연산횟수 + 이번 턴에 -1 한 번
        if i % 2 == 0:
            dp[i] = min(dp[i], dp[i//2] + 1) # //2했을 때 나오는 연산 횟수 + 이번 턴에 //2 한번
        if i % 3 == 0 :
            dp[i] = min(dp[i], dp[i//3] + 1)
        if i % 5 == 0 :
            dp[i] = min(dp[i], dp[i//5] + 1)
            
    print(dp[X])   
main()