# 
from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    N = int(input())
    K = int(input())
    
    left = 1
    right = K
    while left <= right:
        center = (left + right) // 2
        cnt = 0
        for i in range(1,N+1):
            cnt += min(center // i, N)
        if cnt >= K :
            ans = center            
            right = center - 1
        else :
            left = center +1
        print(f'center : {center}')
    print(ans)
        
        
    
    