from itertools import permutations
from sys import maxsize, stdin
input = stdin.readline
# 1. 연산자 배열 만들기 
def makeOperators(arr) :   
    operators = []        
    for i in range(len(arr)): 
        if arr[i] == 0 :continue 
        for _ in range(arr[i]):
            operators.append(arr.index(arr[i]))
            arr[i] -=1
    return operators            
    
if __name__ == "__main__":
    N = int(input())
    nums = list(map(int, input().split()))
    operators = makeOperators(list(map(int, input().split())))
    maxi = -maxsize          
    mini = maxsize
    
    # 2. 연산자 배열 순열
    perm = list(permutations(operators, N-1))
    
    # 3. 계산해서 최대, 최소
    for p in perm :   
        ans = nums[0]
        for j in range(1,len(nums)):
            if p[j-1] == 0:
                ans += nums[j]
            elif p[j-1] == 1:
                ans -= nums[j]
            elif p[j-1] == 2:
                ans *= nums[j]
            else :
                ans = ans // nums[j] if ans >= 0 else -(-(ans) // nums[j]) 
            maxi = max(maxi, ans)
            mini = min(mini, ans)
            
    print(maxi)                 
    print(mini)
    
                

    
                