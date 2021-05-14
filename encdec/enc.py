import random
def keydec(n):
    s=""
    while n>0:
        s+=str(n%2)
        n=n//2
    r=s[::-1]
    le=5-len(r)
    q=""
    q+="0"*le
    q+=r
    ss=""
    for i in q:
        t=random.randint(1,10)
        ss+=chr(64+int(i)+(2*t))
    return ss
s=input()
l=len(s)
p=""
s=s.upper()
k=random.randint(1,10)
key=keydec(k)
x=k
for i in s:
    if i!=" ":
        p+=chr(ord(i)+x)
        x-=2
        if x<1:
            x=k
    else:
        p+="*"
p+=key 
print(p)