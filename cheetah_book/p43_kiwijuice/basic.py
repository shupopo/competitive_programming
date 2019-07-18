capacities = [20, 20]
bottles = [5, 19]
fromId = [0]
toId = [1]
result = [0, 0]

for i in range(len(fromId)):
    juice_sum = bottles[fromId[i]]+bottles[toId[i]]
    if juice_sum <= capacities[toId[i]]:
        result[fromId[i]] = 0
        result[toId[i]] = juice_sum
    else:
        rest = juice_sum - capacities[toId[i]]
        result[fromId[i]] = rest
        result[toId[i]] = capacities[toId[i]]
print(result)
