n=4
i=1
p=""
m=n+((n+1)/2)+1
a=int(m)
while(i<=m and a>0):
    j=i
    l=i
    k=n-1
    o=a
    s=a
    while(j<=n and i<=k):
        while(l>1):
            p+=" "
            l=l-1
        p+=str(j)
        p+=" "
        j=j+1
    while(i>k and o<=n):
        while(s>1):
            p+=" "
            s=s-1
        p+=str(o)
        p+=" "
        o=o+1
    a=a-1
    i=i+1
    p+="\n"
print(p)
            
