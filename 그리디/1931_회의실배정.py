#11:28~
from sys import stdin
input = stdin.readline

def main():
    N = int(input())
    TIME = [list(map(int, input().split())) for _ in range(N)]
    TIME.sort(key=lambda a: (a[0], a[1]-a[0])) # --------------
      

main()