num = 1000
a = [int(i) for i in input().split()]
for i in range(1, len(a)):
    if 0 < a[i] < num:
        num = a[i]
print(num)
