from collections import defaultdict
from operator import itemgetter

total = defaultdict(list)
with open("input.txt", "rt", encodiong="utf8") as f:
    for row in f:
        _class, range = map(int, row.rsplit(None, 2)[-2:])
        total[_class].append(range)

print(*(max(v) for k, v in sorted(total.items(), key=itemgetter(0))))
