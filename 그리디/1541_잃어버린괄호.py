
def main():
    A = input()
    B = A.split("-")
    
    result = [] ;
    for b in B :
        r = 0
        for j in b.split("+"):
            r += int(j)
        result.append(r)
        
    answer = result[0];    
    for i in range(1,len(result)):
        answer -= result[i]
    print(answer)
        
main()

