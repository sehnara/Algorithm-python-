from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    N = int(input())
    potion = list(map(int, input().split()))
    potion.sort()
    
    left = 0
    right = N-1
    total = 2000000000
    final = []   
     
    while left < right:
        a = potion[left] + potion[right]
        if total > abs(a) :
            final = [potion[left], potion[right]]
            total = abs(a);
        
        if a < 0 :
            left += 1
        else : 
            right -=1
    print(*sorted(final))
    
        