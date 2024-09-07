n=11
p=""
for i in range(n):
    for j in range(n):
        if(i>=j and j<=(n/2) and i<=(n/2)):
            p+="*"
        elif((i+j)>=n-1 and j>i and i<=(n/2)):
            p+="*"
        elif((i+j)<=n-1 and j<=(n/2) and i>(n/2)):
            p+="*"
        elif(i<=j and j>(n/2) and i>(n/2)):
            p+="*"
        else:
            p+=" "
    p+="\n"
print(p)
