n=int(input("enter any number"))
res=0
while n>0:
    rem=n%10
    res=res*10+rem
    n//=10
print(res)
    
