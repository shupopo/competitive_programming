def main():

    N = int(input())
    A = [int(s) for s in input().split(" ")]
    ans = 0
    right = 0
    S = set()

    for left in range(N):
        while right < N and (A[right] not in S):
            S.add(A[right])
            right += 1

        ans = max(ans, right - left)
        if left == right:
            right += 1
        else:
            S.remove(A[left])

    print(ans)


if __name__ == '__main__':
    main()
