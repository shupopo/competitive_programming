n = int(input())

a, b = 0, 0
c = 1
if n in [1, 2]:
    c = 0
else:
    for i in range(n-3):
        a, b, c = b, c, (a + b + c) % 10007
print(c)

# a, b, c = b, c, (a + b + c) % 10007
# は余りだけをひたすら生成していく
# an = (an//10007)+(an%10007)
# a+b+c = (a+b+c//10007)+(a + b + c) % 10007
# an = a+b+c より (an//10007) = (a+b+c//10007)
# よって(an%10007) = (a + b + c) % 10007
