from collections import deque
from sys import stdin
input = stdin.readline

row, col = map(int, input().split())
matrix = []
for k in range(row):
    matrix.append(list(map(int, input().strip())))
visited = [[0] * (col) for _ in range(row)]

que = deque([[0,0]])
dx = [-1, 1, 0 ,0]
dy = [0, 0, -1, 1]

while que:
    x,y = que.popleft()
    visited[x][y] = True
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if 0<=nx<=row-1 and 0<=ny<=col-1:
            if not visited[nx][ny] and matrix[nx][ny] == 1:
                que.append([nx,ny])
                matrix[nx][ny] = matrix[x][y] +1
                
print(matrix[-1][-1])
                
                



