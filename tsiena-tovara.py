import math
a = float(input())

rub = int(a)
cop = int(math.ceil(a * 100 - rub * 100))

print("{r} {cc}".format(r=rub, cc=cop))
