l=[]
n=int(input("Enter number of values "))
for i in range(0,n,1):
    x=int(input("Enter value "))
    l.append(x)
for i in range(0,n-1,1):
    for j in range (0,n-1,1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)
