from sys import stdin;
input = stdin.readline;

if __name__ == "__main__":
    prime = [False, False] + [True] * 9999; 
    for i in range(2, int(10001 ** 0.5)+1):
        if prime[i]:
            for j in range(2*i, 10001, i):
                prime[j] = False;
                
    T = int(input());
    for _ in range(T):
        n = int(input());
        for j in range(n//2,1,-1):
            if prime[j] and prime[n-j] :
                print(f"{j} {n-j}");
                break;