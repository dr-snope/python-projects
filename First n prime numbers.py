n = int(input("Enter the value of n: "))
for num in range(2, n + 1, 1):
    track = True
    for i in range(2, num):
        if num % i == 0:
            track = False
            break
    if track:
        print(num)
