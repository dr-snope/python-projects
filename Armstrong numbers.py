num=int(input("Enter any number"))
backup=num #backing up
digits=0
while num>0: #counting the digits
    num=num//10
    digits=digits+1
num=backup #restoring

raised_digit=0
result=0
unit_digit=0

while num>0: #checking
    unit_digit=num%10
    raised_digit=unit_digit**digits
    result=result+raised_digit
    num=num//10
    
if backup==result: #verifying
    print("Given number is armstrong")
else:
    print("Given number is not armstrong")
    
