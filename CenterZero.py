n=7
i=0
j=0
p=""
if(n%2!=0):
    i=0
    while(i<n):
        j=0
        while(j<n):
            if(i==j and (n/2)-.5==i):
                p+="0"
            else:
                p+="#"
            j+=1
        p+="\n"
        i+=1
print(p)