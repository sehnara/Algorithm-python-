from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    N = int(input())
    TOWER = list(map(int, input().split()))
    stack = []
    result = []
    
    for T in range(N) :
        curr = TOWER[T]                
        for s in range(len(stack)-1,-1,-1):
            if TOWER[stack[s]-1] < curr :                
                stack.pop()                
            else :
                break  
                  
        stack.append(T+1)  
        
        if len(stack) == 1:
            result.append(0)
        else :
            result.append(stack[-2])                    
    print(* result)