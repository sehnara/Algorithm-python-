import sys
BRACKETS = sys.stdin.readline().strip()

temp = 1
result = 0
stack = [0]

for b in BRACKETS:
    if b == "(":
        temp *= 2
        stack.append(b)
    elif b == "[":
        temp *= 3
        stack.append(b)
    elif b == ")": 
        k = stack.pop()   
        if k and k == "(" or k == "[":
            result += temp
        temp //= 2
        stack.append(b)
    else : 
        p = stack.pop()
        if p and p == "(" or p == "[":
            result += temp
        temp //= 3
        stack.append(b)
        
if temp == 1:
    print(result)
else :
    print(0)
