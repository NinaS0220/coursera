s = input()
a = [int(s) for s in s.split()]
num = 0
for i in a:
    if int(i) > 0:
        num += 1
print(num)
