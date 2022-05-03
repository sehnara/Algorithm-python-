from sys import stdin;
input = stdin.readline;

if __name__ == "__main__":    
    
    N = int(input());
    # 1. 소수 판별
    prime = [False,False]+ [True] * N;
    for i in range(2, int((N+1)**0.5)+1):
        if prime[i] :
            for j in range(2*i, N+1, i):
                prime[j] = False;
                
    # print('>>>>', len(prime), prime);
    primes = [];   
    
    for k in range(2, len(prime)):
        # print(f"total : {len(prime)+1} // k : {k}")
        if prime[k]:
            primes.append(k);            
    count = 0;
    
    for a in range(len(primes)):
        if primes[a] > N:
            break;
        s = 0;
        for b in range(a, len(primes)):
            if s > N :
                break;
            elif s == N :
                count +=1 ;
                break;
            else :
                s += primes[b]
                
    print(count)
            