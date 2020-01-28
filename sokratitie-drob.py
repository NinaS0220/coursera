n = int(input())
m = int(input())


def ReduceFraction(a, b):
    if a % b == 0:
        return n // b, m // b
    else:
        return ReduceFraction(b, a % b)

print(*ReduceFraction(n, m))
