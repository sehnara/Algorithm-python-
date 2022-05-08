from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    row, col = map(int,input().split())
    matrix = [input().strip() for _ in range(row)]
    visited = [[False] * (col) for _ in range(row)]
    count = 0
    dx = [-1, 1, 0 , 0]
    dy = [0, 0, -1, 1]
    
    def dfs(r,c):
        for k in range(4):
            rx = r + dx[k]
            ry = c + dy[k]
            
            if (0<=rx<=(row-1) and 0<=ry<=(col-1)) and (matrix[rx][ry] == '0'):
                if not visited[rx][ry] :                    
                    visited[rx][ry] = True
                    dfs(rx,ry)
    
    for i in range(row):
        for j in range(col):
            if not visited[i][j] and matrix[i][j] == '0':                
                count += 1
                visited[i][j] = True
                dfs(i,j)     
                # for d in range(row):
                #     print(visited[d])
                # print()    
    print(count)                 
    
    
    
    