s = input()
pos = s.find(' ')
print(s[pos:] + ' ' + s[:pos+1])
