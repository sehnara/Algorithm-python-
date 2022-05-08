# 23:16 ~ 23:40 (24m)
from sys import stdin
input = stdin.readline;

def binary_search(arr, x):
    left = 0
    right = len(arr) -1   
    
    while left <= right :        
        center = (left + right) // 2
        if arr[center] > x :
            right = center -1 
        elif arr[center] < x :
            left = center +1
        else :
            return 1        
    return 0

if __name__ == "__main__":
    N = int(input())
    nrr = sorted(list(map(int, input().split())))
    M = int(input())
    mrr = list(map(int, input().split()))
    for i in range(M):
        print(binary_search(nrr, mrr[i]))
        
    
    