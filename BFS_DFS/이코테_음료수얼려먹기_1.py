from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    row, col = map(int,input().split())
    matrix = [input().strip() for _ in range(row)]
    # 1. matrix는 이미 0과 1로 나뉘어져, visited를 따로 선언해줄 필요없다.
    # visited = [[False] * (col) for _ in range(row)] 
    count = 0
    dx = [-1, 1, 0 , 0]
    dy = [0, 0, -1, 1]
    
    def dfs(r,c):
        for k in range(4):
            rx = r + dx[k]
            ry = c + dy[k]
            
            if (0<=rx<=(row-1) and 0<=ry<=(col-1)):
                if matrix[rx][ry] == '0' :                    
                    matrix[rx][ry] = '1'
                    dfs(rx,ry)
    
    for i in range(row):
        for j in range(col):
            # 2. 이 구조가 dfs 내부 구조와 반복된다. 줄일 수 있을 듯
            if matrix[i][j] == '0':                
                count += 1
                matrix[i][j] = '1'
                dfs(i,j)     
                # for d in range(row):
                #     print(visited[d])
                # print()    
    print(count)                 
    
    
    
    