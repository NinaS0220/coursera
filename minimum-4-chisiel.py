def min4(a, b, c, d):
    e = min(a, b)
    f = min(c, d)
    m = min(e, f)
    return m

a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(min4(a, b, c, d))
