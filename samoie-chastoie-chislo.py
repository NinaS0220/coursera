a = list(map(int, input().split()))
max = a[0]
max_count = a.count(max)
for i in a:
    if a.count(i) > max_count:
        max = i
        max_count = a.count(i)
print(max)
