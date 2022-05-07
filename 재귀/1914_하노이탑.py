k = int(input())
a = 1
b = 3
count = 0 

def hanoi(k,a,b):
    if k > 1:
        hanoi(k-1, a, 6-a-b)
    print(a,b)
    if k > 1:
        hanoi(k-1, 6-a-b,b)

print(count)
if k <=20 :
    hanoi(k,a,b)
