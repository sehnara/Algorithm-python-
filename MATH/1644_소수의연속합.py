from sys import stdin;
input = stdin.readline;

def get_prime(n):
    prime = [False,False]+ [True] * n;
    for i in range(2, int((n+1)**0.5)+1):
        if prime[i] :
            for j in range(2*i, n+1, i):
                prime[j] = False;
    return [k for k in range(2,n+1) if prime[k] == True];

if __name__ == "__main__":   
    N = int(input());
    primes = get_prime(N);
    count = 0;
    
    for a in range(len(primes)):  
        s = 0;
        for b in range(a, len(primes)):
            s += primes[b];
            if s > N :
                break;
            elif s == N :
                count +=1 ;
                break;               
        
    print(count)
            