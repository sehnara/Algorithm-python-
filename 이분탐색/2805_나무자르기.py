# 01:32 ~ 01:45 (13m)
from sys import stdin
input = stdin.readline

def cutTree(cut):
    s = 0;
    for t in trees:
        if t >= cut :
          s += t-cut
        else :
            continue
    return s

def binarySearch():
    left = 0
    right = max(trees)
    maxi = 0;
    while left <= right:
        center = (left + right) // 2
        if cutTree(center) >= M:
            left = center +1
            maxi = max(maxi, center)
        else :
            right = center -1 
    print(maxi)    

if __name__ == "__main__":
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))
    binarySearch()

    
    
    
    