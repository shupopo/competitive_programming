N = int(input())
ng_numbers = [int(input()) for _ in range(N)]

ng_numbers.sort()
ng_numbers.reverse()

if N in ng_numbers:
    print("NO")
    exit()
pattern = ""
if ng_numbers[0] == ng_numbers[1] + 1:
    if ng_numbers[1] == ng_numbers[2] + 1:
        if N < ng_numbers[2]:
            print("YES")
        else:
            print("NO")
    elif ng_numbers[1] == ng_numbers[2] + 2:
        pattern = "A"
    else:
        pattern = "B"
elif ng_numbers[0] == ng_numbers[1] + 2:
    if ng_numbers[1] == ng_numbers[2] + 1:
        pattern = "C"
    elif
count = 0
while N > 0 and count < 101:
    if N == 0:
        print("YES")
        exit()
    if N in ng_numbers:

    count += 1

print("NO")
