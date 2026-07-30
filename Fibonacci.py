n=int(input("enter to no of terms "))
b=1
a=0
print(a,b,sep="\n",end="\n")
for i in range(2,n,1):
    c=a+b
    print(c,end="\n")
    a=b
    b=c
