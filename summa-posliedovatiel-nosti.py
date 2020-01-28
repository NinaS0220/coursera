n = 0


def sum_posl(n):
    n = int(input())
    if n == 0:
        return 0
    return n + sum_posl(n)

print(sum_posl(n))
