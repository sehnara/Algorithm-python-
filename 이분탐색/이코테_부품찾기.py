# 14:08 ~ 14:24
from sys import stdin
input = stdin.readline

def binary_search(arr, target, result):
    start = 0
    end = len(arr)-1

    while start <= end :
        center = (start + end) // 2
        if arr[center] > target:
            end = center -1
        elif arr[center] < target:
            start = center + 1
        else :
            result.append("yes")
            return # ------------------- 끝내줘야 한다.
    result.append("no")
    return
        

def main():
    N = int(input())
    MARKET = sorted(list(map(int, input().split())))
    M = int(input())
    CUSTOMER = list(map(int, input().split()))
    result = []
    for c in CUSTOMER : 
        binary_search(MARKET, c, result)
        
    print(result)    
main()