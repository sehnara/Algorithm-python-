from sys import stdin
input = stdin.readline

if __name__ == "__main__": 
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    count = [0,0]
    
    def div(x, y, n):
        baro = matrix[x][y]
        
        for i in range(x, x+n): # ___________ 이 범위를 또 놓치네
            for j in range(y, y+n): # ___________ 이 범위를 또 !!!! 놓치네
                if matrix[i][j] != baro:
                    div(x, y, n//2)
                    div(x + n//2, y, n//2)
                    div(x, y + n//2 , n//2)
                    div(x + n//2, y + n//2, n//2)
                    return
        count[baro] += 1

    div(0,0,N)
    print(count[0])
    print(count[1])