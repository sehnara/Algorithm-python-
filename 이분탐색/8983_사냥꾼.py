from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    M, N, L = map(int, input().split()) # M : 사대 수 / N : 동물 수 / L : 사정거리
    hunters = sorted(list(map(int, input().split()))) # 사대의 위치
    targets = [list(map(int, input().split())) for _ in range(N)] # 동물의 위치
    count = 0
    
    for i in range(N):
        if targets[i][1] > L :
            continue
        mini = 0 if targets[i][0] - (L - targets[i][1]) < 0 else targets[i][0] - (L - targets[i][1])
        maxi = targets[i][0] + (L-targets[i][1])

        left = 0
        right = M-1
        
        while left <= right:
            center = (left + right)  // 2
            
            if mini <= hunters[center] <= maxi:
                count +=1
                break
            elif hunters[center] < mini :
                left = center + 1
            else :
                right = center - 1
            
    print(count)
                
            
            
            
            
             
    
    
    