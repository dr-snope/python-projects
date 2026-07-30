n=int(input("Enter number "))
x=n
factorial=1
while n>0:
    factorial*=n
    n-=1
print(f'Factorial of {x} is {factorial}')
