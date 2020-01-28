s = input()
pos1 = s.find('h')
b = s[::-1]
pos2 = len(b) - b.find('h') - 1

print(s[:pos1] + s[pos2+1:])
