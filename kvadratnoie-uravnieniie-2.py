import math
a = float(input())
b = float(input())
c = float(input())

discr = b ** 2 - 4 * a * c
if a != 0:
    if discr > 0:
        x1 = (-b + math.sqrt(discr)) / (2 * a)
        x2 = (-b - math.sqrt(discr)) / (2 * a)
        if x1 <= x2:
            print("{} {} {}".format(2, x1, x2))
        else:
            print("{} {} {}".format(2, x2, x1))
    elif discr == 0:
        x = -b / (2 * a)
        print("{} {}".format(1, x))
    else:
        print(0)
else:
    if b == 0 & c == 0:
        print(3)
    elif b != 0:
        r1 = -c / b
        print("{} {}".format(1, r1))
    else:
        print(0)
