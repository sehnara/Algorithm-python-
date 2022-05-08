# 15:31 ~ 16:05(34m)
from sys import stdin
input = stdin.readline

def cut_lan(lans, m):
    s = 0
    for l in lans:
        s += l // m
    return s    

def binary_search(lans):
    left = 1 # 1로 잡아야 하네?
    right = max(lans) # 왜 max로 잡아야 하는거지?
    maxi = 0
    while left <= right : 
        center = (left + right) // 2            
        if cut_lan(lans, center) >= N : 
            left = center +1       
            maxi = max(maxi, center)           
        else :
            right = center - 1                     
    return maxi

if __name__ == "__main__":     
    K, N = map(int, input().split())
    lans = [int(input()) for _ in range(K)]
    print(binary_search(lans))
    