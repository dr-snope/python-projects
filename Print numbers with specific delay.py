import time
n=int(input("enter end number "))
x=float(input("enter delay "))
for i in range(1,n+1,1):
    time.sleep(x)
    print(i)
