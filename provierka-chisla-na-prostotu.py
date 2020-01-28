# -coding:utf-8
# сложность алгоритма O(корень из n):
def IsPrime(n):
    d = 2
    while d * d <= n and n % d != 0:
        print(d, d*d, n%d)
        d += 1
    return d * d > n

if IsPrime(int(input())):
    print("YES")
else:
    print("NO")
