a = list(map(int, input().split()))
min_a = max_a = 0
for i in range(1, len(a)):
    if a[i] < a[min_a]:
        min_a = i
    if a[i] > a[max_a]:
        max_a = i
a[max_a], a[min_a] = a[min_a], a[max_a]
print(' '.join([str(i) for i in a]))
