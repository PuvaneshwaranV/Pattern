n=5
p=""
k=1
l=1
for i in range(n):
    for j in range(k):
        p+=str(l)
        if(l<10):
            p+="  "
        else:
            p+=" "
        l=l+1
    p+="\n"
    k=k+1
print(p)  
