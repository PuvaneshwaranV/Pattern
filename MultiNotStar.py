#MULTIPLY
import re
n1=input("Enter the Value")
n2=input("Enter the Value")
n=0
i=1
def is_number(string):
    pattern = r'^-?\d+$'
    return bool(re.match(pattern, string))
p=is_number(n1)
q=is_number(n2)
if(p and q ):
    if(n1[0]=='-' and n2[0]=='-'):
        n1=n1[1:]
        n2=n2[1:]
    elif(n2[0]=='-'):
        n3=n2
        n2=n1
        n1=n3
    n1=int(n1)
    n2=int(n2)
    if(n1!=0 or n2!=0):
        while(i<=n2):
            n+=n1
            i+=1
        print(n)
    else:
        print(n)
else:
    print("Input should be only Integer")

