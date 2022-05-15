from collections import deque
from sys import stdin
input = stdin.readline  

def main():
    N = int(input())    
    CARD = deque()
    for i in range(1,N+1):
        CARD.append(i)
    
    if len(CARD) == 1:
        print(CARD[0])
        return
    
    while CARD:
        CARD.popleft()
        if len(CARD) == 1:
            print(CARD[0])
            break
        CARD.append(CARD.popleft())
main()