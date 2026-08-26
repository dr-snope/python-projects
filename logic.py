def is_armstrong(value:int):
    backup = value
    digits = 0
    while value > 0:
        value //= 10
        digits += 1
    value = backup

    raised_digit = 0
    result = 0
    unit_digit = 0

    while value > 0:
        unit_digit = value % 10
        raised_digit = unit_digit ** digits
        result += raised_digit
        value //= 10
        
    if backup == result:
        return True
    else:
        return False

def bubble_sort(array:list[int]):
    for i in range(0,len(array)-1,1):
        for j in range (0,len(array)-1,1):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
    return array

def factorial(value:int):
    fact=1
    while value>0:
        fact *= value
        value -= 1
    return fact

def is_prime(value:int):
    for i in range (2, value):
        if value % i == 0:
            return False
    return True

    

