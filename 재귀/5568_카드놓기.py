N = int(input())
K = int(input())
nums = []
for _ in range(N):
    nums.append(input())
result = []

def dfs(answer, n, visited):
    if visited.count(True) == K :
        result.append(answer)
        return  
    visited[n] = True
    answer += nums[n]
    for j in range(N):
        if not visited[j]:
            dfs(answer, j, visited)        

for i in range(N):
    visited = [False] * (N+1)
    answer = ''
    dfs(answer, i, visited)
print(len(set(result)))