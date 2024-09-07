n=6 
i=1
p=""
while(i<=n):
    j=i
    k=i
    while(j<=n):
        while(k>1):
            p+=" "
            k=k-1
        p+=str(j)
        p+=" "
        j=j+1
    p+="\n"
    i=i+1 
print(p)
