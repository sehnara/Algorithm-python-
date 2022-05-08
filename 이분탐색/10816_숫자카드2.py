# [시간 초과]
from sys import stdin
input = stdin.readline

def binary_search(m):
    left = 0
    right = len(nrr)-1
    
    while left <= right:
        center = (left + right) // 2
        if nrr[center] < m :
            left = center + 1
        elif nrr[center] > m:
            right = center -1
        else :         
            result.append(nrr[left:right+1].count(m))
            return
    result.append(0)
    return
        
if __name__ == "__main__":
    N = int(input())
    nrr = sorted(list(map(int, input().split())))
    M = int(input())
    mrr = list(map(int, input().split()))
    result = []
    for m in mrr:       
        binary_search(m)
    print(* result)
    
    