lst = list(map(int, input().split()))
x = int(input())
ind = 0
while ind < len(lst) and lst[ind] >= x:
    ind += 1
print(ind + 1)
