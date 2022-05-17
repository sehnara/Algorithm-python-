# 14:25 ~ 14:31 (계수 정렬)
from sys import stdin
input = stdin.readline

def main():
    N = int(input())
    MARKET = list(map(int, input().split()))
    M = int(input())
    CUSTOMER = list(map(int, input().split()))
    SEARCHED = [0] * (max(MARKET)+1)

    for M in MARKET : 
        SEARCHED[M] += 1
    
    for i in CUSTOMER:
        if SEARCHED[i] != 0 :
            print("yes", end = " ")
        else :
            print("no", end=" ")
        
main()