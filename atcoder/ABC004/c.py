N = int(input())
cards = [1, 2, 3, 4, 5, 6]
r = N % 30
for i in range(r):
    index1 = i % 5
    index2 = i % 5 + 1
    tmp = cards[index1]
    cards[index1] = cards[index2]
    cards[index2] = tmp

ans = ""
for card in cards:
    ans += str(card)
print(ans)
# print(*cards,sep='')

"""
解説https://www.slideshare.net/chokudai/abc004demoでも実験→実装

"""
