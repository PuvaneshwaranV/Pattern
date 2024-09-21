n=input("Enter the Value")
i=0
j=0
p=""
i=0
if(n.isdigit() or n[0]=='-' and n[1:].isdigit()):
    n=int(n)
    if(n>0):
        while(i<n):
            j=0
            while(j<n):
                if(i==j):
                    p+="*"
                else:
                    p+="$"
                j=j+1
            p+="\n"
            i=i+1
    else:
        print("Value must be greater than 0")
else:
     print("Please enter the digit only")
print(p)
