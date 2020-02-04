from collections import defaultdict, Counter

lines = open('input.txt')

dct = defaultdict(Counter)
for line in lines:
    customer, product, count = line.split()
    dct[customer][product] += int(count)

for customer, sales in sorted(dct.items(), key=lambda x: x[0]):
    print(customer, ':', sep='')
    for product, count in sorted(sales.items(), key=lambda x: x[0]):
        print(' {} {}'.format(product, count))
