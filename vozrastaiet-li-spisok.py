def IsAscending(A):
    i = 1
    while i <= len(A) - 1 and A[i] > A[i - 1]:
        i += 1
    return print('YES') if i == len(A) else print('NO')

A = [int(i) for i in input().split()]
IsAscending(A)
