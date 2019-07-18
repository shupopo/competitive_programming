inputs = [int(i) for i in input().split(" ")]

k = inputs[3]
primes = [inputs[0],inputs[1],inputs[2]]

other_primes = [2,3,5,7,11,13,15,17,19,23,29,31,37,41,43,47,53]

for prime in primes:
    other_primes.remove(prime)

def is_not_factorable(n,primes,other_primes):
    for prime in other_primes:
        if n % prime==0:
            return True
    if n > 1 and n%primes[0] !=0 and n%primes[1] !=0 and n%primes[2] !=0 :
        return True
    for i in range(len(primes)):
        b = primes[i]
        while n % b == 0:
            n = n // b
    if n > 1:
        return True
    return False


progression = []
target = 1
for i in range(k):
    while is_not_factorable(target,primes,other_primes):
        target += 1
    progression.append(target)
    target += 1

print(progression[k-1])
