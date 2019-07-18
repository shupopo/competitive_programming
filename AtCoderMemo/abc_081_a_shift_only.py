N = input()
An = [int(i) for i in input().split()]
isOdd = False
count = 0
while True:
    for num in An:
        if num % 2 == 1:
            isOdd = True
    if isOdd == False:
        for num in An:
            An[An.index(num)]  = int(num/2)
        count += 1
    else:
        break
print(count)
