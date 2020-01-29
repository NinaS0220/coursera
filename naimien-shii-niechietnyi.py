num = 999999999
a = [int(i) for i in input().split()]
for i in range(0, len(a)):
    if a[i] < num and a[i] % 2 != 0:
        num = a[i]
print(num)
