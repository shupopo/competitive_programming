n = int(input())
input_numbers = []
for i in range(n):
    input_numbers.append(input())

for i in range(n):
    card_numbers = list(input_numbers[i])
    total_even_numbers = 0
    total_odd_numbers = 0
    for i in range(len(card_numbers)):
        if i % 2 == 0:
            if int(card_numbers[i]) * 2 < 10:
                total_even_numbers += int(card_numbers[i]) * 2
            else:
                nums = list(str(int(card_numbers[i])*2))
                total_even_numbers += int(nums[0])+int(nums[1])
        else:
            if i == 15:
                continue
            else:
                total_odd_numbers += int(card_numbers[i])
    X = 0
    remainder = (total_even_numbers+total_odd_numbers) % 10
    if remainder!= 0:
        X = 10 - remainder
    print(X)

