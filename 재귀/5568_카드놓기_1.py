N = int(input())
K = int(input())
nums = [input() for _ in range(N)]

tmp = []
result = []
visited = [False] * N

def dfs(depth):
    global tmp
    if depth == K:
        result.append("".join(map(str,tmp)))
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            tmp.append(nums[i])
            dfs(depth+1)
            visited[i] = False
            tmp.pop()
    
dfs(0)
# print(result)
print(len(set(result)))
