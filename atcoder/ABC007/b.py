A = input()
answer = ""
if A == "a":
    answer = -1
elif len(A) == 1:
    answer = "a"
else:
    for i in range(len(A)-1):
        answer += A[i]
print(answer)
