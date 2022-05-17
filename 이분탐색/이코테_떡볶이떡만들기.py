# 14:32 ~ 
from sys import stdin
input = stdin.readline

def cut(arr, center):
    result = 0
    for i in arr:
        result += i-center if center <= i else 0
    return result 

def main():
    N, M = map(int, input().split())
    RICE_CAKE = list(map(int, input().split()))
    start = 0
    end = max(RICE_CAKE)
    maxi = 0
    while start <= end:
        center = (start + end) // 2
        if cut(RICE_CAKE, center) >= M : # ----------- 이 조건에 의해 left, right의 값 변화를 반대로 주고 있었다.
            start = center + 1 # 이 경우 자르는 길이가 줄어들 수록 나오는 떡은 더 많아 진다. 
            maxi = max(maxi, center)
        elif cut(RICE_CAKE, center) < M :
            end = center - 1
        
    
    
main()