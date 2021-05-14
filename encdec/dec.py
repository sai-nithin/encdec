def fun(binary): 
      
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return(decimal)
s=input()
sol=""
l=len(s)-5
a=""
key=""
for i in range(l):
    a+=s[i]
for i in range(l,l+5):
    key+=str(ord(s[i])%2)
#print(a)
k=int(key)
k=fun(k)
d=k
for i in a:
    if i!="*":
        sol+=chr(ord(i)-k)
        k-=2
        if k<1:
            k=d 
    else:
        sol+=" "
print(sol)
