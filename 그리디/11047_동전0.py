# 19:15~19:40(25m)
# 거꾸로 for문 돌아야 loop를 두 번 안 돈다. 이게 K가 1억까지인데 시간은 1초니까 한 번 돌 시간 밖에 없음

from sys import stdin
input = stdin.readline

def main():
    N, K = map(int, input().split())
    COINS = [int(input()) for _ in range(N)]
    count = 0
    
    
    for c in range(len(COINS)-1, -1, -1):
        coin = COINS[c]
        if coin <= K : 
            count += K // coin
            K = K % coin
    print(count)
main()