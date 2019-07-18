N = int(input())
cards = [1, 2, 3, 4, 5, 6]
for i in range(N):
    index1 = i % 5
    index2 = i % 5 + 1
    tmp = cards[index1]
    cards[index1] = cards[index2]
    cards[index2] = tmp


ans = ""
for card in cards:
    ans += str(card)
print(ans)
