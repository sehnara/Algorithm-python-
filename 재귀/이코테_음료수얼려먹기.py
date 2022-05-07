#20:21~
from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    row, col = map(int, input().split())
    matrix = [input().strip() for _ in range(row)]
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    visited = [[False] * (col+1) for _ in range(row+1)]
    count = 0;
    
    def dfs(matrix, x, y, visited):
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            
            if 0<=nx<=col-1 and 0<=ny<=row-1:
                if matrix[nx][ny] == '1' :
                    continue
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    dfs(matrix, nx, ny, visited)
                    
    
    for i in range(row):
        for j in range(col):
            if not visited[i][j] :
                if matrix[i][j] == '0':
                    count +=1
                    dfs(matrix, 0, 0, visited)
                    
    print(count)
    