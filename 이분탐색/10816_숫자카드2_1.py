from sys import stdin
input = stdin.readline

def binary_search(mrr, n):
    left = 0
    right = len(mrr)-1
    
    while left <= right:
        center = (left + right) // 2
        if mrr[center] < n :
            left = center + 1
        elif mrr[center] > n:
            right = center -1
        else :
            return True    
    return False
        
if __name__ == "__main__":
    N = int(input())
    nrr = list(map(int, input().split()))
    M = int(input())
    mrr = list(map(int, input().split()))
    dict = {}
    
    for n in nrr:
        if binary_search(sorted(mrr), n):
            if n in dict : 
                dict[n] +=1
            else :
                dict[n] = 1            
    
    for m in mrr :
       try : 
           print(dict[m], end = " ")
       except : 
          print(0, end=" ")  