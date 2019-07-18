first = ["snakes", "programming", "cobra", "monty"]
second = ["python", "python", "anaconda", "python"]
count = {}

for item in first:
    count[item] = 0

for item in second:
    count[item] = 0

for i in range(len(first)):
    count[first[i]] += 1
    count[second[i]] += 1

print(max((v, k) for k, v in count.items())[1])
