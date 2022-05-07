from itertools import permutations
from sys import maxsize, stdin
input = stdin.readline
def calc(arr):
        result = 0
        for i in range(1,N):
            result += abs(arr[i-1] - arr[i])
        return result    
    
if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))
    perm = list(permutations(arr, N))
    maxi = -maxsize
    for a in perm:
        maxi = max(maxi, calc(a))
        
    print(maxi)
        
    