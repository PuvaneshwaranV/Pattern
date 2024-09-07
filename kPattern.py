n=7
m=(2*n)-1
i=1
p=""
while(i<=m):
    if(i<=n):
        j=n-i+1
        while(j>0):
            p+="* "
            j=j-1
    elif(i>n):
        j=i-n+1
        while(j>0):
            p+="* "
            j=j-1
    p+="\n"
    i=i+1
print(p)
        
