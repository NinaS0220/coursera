import math
a = float(input())
b = float(input())
c = float(input())

discr = b ** 2 - 4 * a * c

if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2 * a)
    x2 = (-b - math.sqrt(discr)) / (2 * a)
    if x1 <= x2:
        print("{} {}".format(x1, x2))
    else:
        print("{} {}".format(x2, x1))
elif discr == 0:
    x = -b / (2 * a)
    print(x)
else:
    print(" ")
