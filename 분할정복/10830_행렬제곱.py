from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    N, B = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    def proc(arr, brr):
        temp = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):                
                for k in range(N):
                    temp[i][j] += (arr[i][k] * brr[k][j])
                temp[i][j] = temp[i][j] % 1000
        return temp

    def square(arr, b):
        if b == 1:  # 1의 경우를 생각한 점
            for i in range(N):
                for j in range(N):
                    arr[i][j] %= 1000                    
            return arr
    
        temp = square(arr, b // 2) # 재귀를 이런 식으로 쓴다는 점
        if b % 2 == 0 :
            return proc(temp, temp)
        else:
            return proc(proc(temp, temp),matrix)
                
    for s in range(N):
        print(* square(matrix, B)[s])
   
    

        
            
        