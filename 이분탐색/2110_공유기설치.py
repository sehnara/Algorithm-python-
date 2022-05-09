# 14:06 ~ 
from locale import currency
from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    N, C = map(int, input().split())
    HOUSE = sorted([int(input()) for _ in range(N)])
    HOUSE.sort()
    res = 0
    # 이 문제의 left, right는 최소거리와 최대거리
    # center는 최대거리라고 개념을 잡는게 중요
    
    left = 1
    right = HOUSE[-1] - HOUSE[0]
    
    while left <= right : 
        center = (left+ right) // 2
        curr = HOUSE[0]
        count = 1
        
        for i in range(1,N):
            if HOUSE[i] - curr >= center:
                count +=1
                curr = HOUSE[i]
        
        if count >= C:
           res = center
           left = center+1
        else :
            right = center-1
    print(res) 
                
    
    
    
    