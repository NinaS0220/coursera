import math
p = int(input())
x = int(input())
y = int(input())

num = float(str(x) + '.' + str(y))
p = float(p)/100
sum = num * p
a = num + sum
rub = int(a)
cop = int(math.floor(a * 100 - rub * 100))
print("{r} {cc}".format(r=rub, cc=cop))
