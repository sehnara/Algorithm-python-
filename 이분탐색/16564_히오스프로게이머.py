from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().split()) # N : 캐릭터 수, K : 레벨 올릴 수 있는 양
    levels = [int(input()) for _ in range(N)]
    
    left = min(levels)
    right = max(levels) + K
    maxi = 0
    while left <= right :  # ------------- 이거 범위 확실히 하자
        center = (left + right)  // 2
        tot = 0
        for level in levels:
            if level >= center :
                continue    
            else : 
                tot += (center - level)
                
        if tot <= K : # --------------- 이 범위 확실히 하자
            left = center + 1      
            maxi = max(maxi, center)
        elif tot > K :
            right = center - 1  
        
    print(maxi)
            

        
    
    