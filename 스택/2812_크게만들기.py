from sys import stdin
input = stdin.readline

def main():
    N, K = map(int, input().split())
    NUM = input().strip()
    stack = [0]*K
    delNum = 0
    
    for i in range(N):
        while stack and stack[-1] < int(NUM[i]):        
            stack.pop()         
            delNum += 1
            
            if delNum == K :
                for _ in range(i, N):
                    stack.append(int(NUM[i]))
                print("".join(map(str,stack)))
                return        
               
        stack.append(int(NUM[i]))              
    print("".join(map(str,stack)))
    
main()