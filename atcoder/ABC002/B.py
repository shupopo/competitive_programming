import copy
char_list = list(input())

char_list2 = copy.copy(char_list)

for c in char_list:
    if c in ["a", "i", "u", "e", "o"]:
        char_list2.remove(c)
print("".join(char_list2))
