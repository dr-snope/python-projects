l=[]
n=int(input("Enter number of values "))
for i in range(0,n,1):
    x=int(input("Enter value "))
    l.append(x)
i=0
j=n//2
c=0
while c<n//2:
    l[i],l[j]=l[j],l[i]
    i=i+1
    j=j+1
    c=c+1
print(l)
