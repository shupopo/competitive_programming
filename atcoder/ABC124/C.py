char_list = list(input())
count1 = 0
count2 = 0
if len(char_list) == 1:
    print(0)
else:
    for i in range(len(char_list)):
        if i % 2 == 0:
            if char_list[i] is "0":
                continue
            else:
                count1 += 1
        else:
            if char_list[i] is "1":
                continue
            else:
                count1 += 1
    for i in range(len(char_list)):
        if i % 2 == 0:
            if char_list[i] is "1":
                continue
            else:
                count2 += 1
        else:
            if char_list[i] is "0":
                continue
            else:
                count2 += 1
    print(min(count1,count2))