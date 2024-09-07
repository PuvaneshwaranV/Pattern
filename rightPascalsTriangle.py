n=10
p=""
i=1
while(i<=n):
    j=i
    if((i%2)!=0):
        while(j>0):
            if((j%2)!=0):
                p+="*"
                p+=" "
            else:
                p+="  "
            j=j-1
    else:
        while(j>0):
            if((j%2)!=0):
                p+="*"
                p+=" "
            else:
                p+="  "
            j=j-1
    p+="\n"
    i=i+1
k=n-1
while(k>0):
    l=k
    if((k%2)!=0):
        while(l>0):
            if((l%2)!=0):
                p+="*"
                p+=" "
            else:
                p+="  "
            l=l-1
    else:
        while(l>0):
            if((l%2)!=0):
                p+="*"
                p+=" "
            else:
                p+="  "
            l=l-1
    p+="\n"
    k=k-1
print(p)
        
