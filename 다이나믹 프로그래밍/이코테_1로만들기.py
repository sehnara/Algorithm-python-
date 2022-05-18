from sys import stdin
input = stdin.readline

def main():
    X = int(input())
    counts = []
    count = 1
    def recur(X, count): 
        brr = [0] * 4
        brr[0] = X // 5 if X % 5 == 0 else -1
        brr[1] = X // 3 if X % 3 == 0 else -1
        brr[2] = X // 2 if X % 2 == 0 else -1
        brr[3] = X - 1 if X - 1 >= 1  else -1
        
        for i in brr:
            if i == 1:
                counts.append(count)
            if i != -1 :                
                recur(i, count + 1)
            
    recur(X,count)
    print(min(counts))
main()