n=10
p=""
for i in range(n):
    k=n-i
    while(k>0):
        p+=" "
        k=k-1
    for j in range(i+1):
        if(j==0 or j==i):
            p+=str(1)
            p+=" "
        else:
            p+=str(i)
            p+=" "
    p+="\n"
print(p)
        
