from collections import deque
from sys import stdin   
input = stdin.readline

def main():
    N = int(input()); K = int(input()); # board 크기 # 사과 개수
    APPLE = [list(map(int, input().split())) for _ in range(K)]; # 사과 위치
    matrix = [[0]*N for _ in range(N)]
    for a,b in APPLE :
        matrix[a][b] = 1   
        
    L = int(input()) # 뱀의 방향 변환 횟수
    DIREC = []    
    for _ in range(L):
        sec, dir = map(str, input().split())
        DIREC.append((int(sec), dir))
    
    T = 0; # 시간
    SNAKE = deque()
    SNAKE.append([0,0])
    D = 0 # 방향 알려줌
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    result = 0
    while True:
        T += 1
        x,y = SNAKE[-1];
        nx = x + dx[D]
        ny = y + dy[D]
        
        if 0<= nx <= N-1 and 0<= ny <= N-1:
            if [nx, ny] in SNAKE :
                result = T
                break;
            if matrix[nx][ny] :
                SNAKE.append([nx, ny]);
                matrix[nx][ny] = 0
            else:
                SNAKE.popleft()
                SNAKE.append([nx, ny])    
        else :
            result = T
            break      

        for t in DIREC:
            if t[0] == T :
                D = D + 1 if t[1] == "D" else D - 1 if D < 4 else  0 
    print(result)
            
main()