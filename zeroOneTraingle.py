n=5
p=""
for i in range(n):
    k=i
    if(i%2!=0):
        while(k>=0):
            if(k%2!=0):
                p+='0'
            else:
                p+='1'
            k=k-1
    else:
        while(k>=0):
            if(k%2!=0):
                p+='0'
            else:
                p+='1'
            k=k-1
    p+="\n"
print(p)
        
