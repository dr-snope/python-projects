n=int(input("Enter any number"))
d=2
flag=0
while d<n:
    if n%d==0:
        flag=1
        break
    d=d+1
if flag==0:
    print("Prime")
else:
    print("Not prime")
