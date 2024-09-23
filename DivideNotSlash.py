
#DIVIDE
import re
m1=input("Enter the Dividend ")
m2=input("Enter the Divisor ")
r=0
q=0
n=0
def is_number(string):
    pattern = r'^-?\d+$'
    return bool(re.match(pattern, string)) 
if(is_number(m1) and is_number(m2)):
    if(m1[0]=='-' and m2[0]=='-'):
        m1=m1[1:]
        m2=m2[1:]
    elif(m1[0]=='-'):
        m1=m1[1:]
        n+=1
    elif(m2[0]=='-'):
        m2=m2[1:]
        n+=1
    m1=int(m1)
    m2=int(m2)
    if(m1!=0 and m2!=0):
        while(m2<=m1):
            m1-=m2
            q+=1
        if(q>0 and n==0):
            r=m1
            print(q)
            print(r)
        elif(q>0 and n==1):
            r=m1
            q=-q
            print(q)
            print(r)
        else:
            print("Dividend must be greater than Divisor")
    elif(m1==0):
        print("0")
    else:
        print("Undefined")
else:
    print("Input must be an Integer")
