s = input()
pos1 = s.find('f')
b = s[::-1]
pos2 = len(b) - b.find('f') - 1
print(pos1, pos2)
if pos1 != pos2 and pos1 != -1:
    print(pos2)
elif pos1 == -1:
    print(-2)
else:
    print(-1)
