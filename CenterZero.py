n=input("Enter the Value")
i=0
j=0
p=""
if(n.isdigit() or n[0]=='-' and n[1:].isdigit()):
    n=int(n)
    if(n>0):
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
        else:
            print("Input should be an odd number")
    else:
        print("Input should be greater than 0")
else:
    print("Input should be only a digits")
print(p)