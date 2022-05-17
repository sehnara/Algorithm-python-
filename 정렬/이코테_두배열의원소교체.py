N, K = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())),reverse=True)

for i in range(K):
    if A[i] < B[i]: # ------------이 경우 생각 못했노... 방심하지말자
        A[i] = B[i]
    else :
        break
    
print(sum(A))


    
    
