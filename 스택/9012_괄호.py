from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    T = int(input())
    VPS = [input().strip() for _ in range(T)]
    
    for i in range(len(VPS)):
        count = 0
        target = VPS[i]
        for j in range(len(target)):
            if target[j] == "(":
                count += 1
            else :
                count -= 1
                
            if count < 0:                
                break
        if count != 0 :
            print("NO")
        else :
            print("YES")