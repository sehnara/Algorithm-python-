from collections import deque

def main():
    N, K = map(int, input().split())
    NUMBER = deque()
    result = []
    for n in range(1,N+1):
        NUMBER.append(n)

    while NUMBER:
        i = K-1
        while i > 0 : 
            NUMBER.append(NUMBER.popleft())
            i -=1        
        result.append(NUMBER.popleft())
        
    if len(result) == 1:
        print(f"<{result[0]}>")
    else : 
        print(f"<{', '.join(map(str, result[:-1]))}, {result[-1]}>")
main()
