m = open('input.txt','r')
n = m.read().splitlines()

encoded = []
for line in n:
    if '\\' in line and '"' not in line:
        a = line.replace('\\','\\\\')
        a = '\"{}\"'.format(a)
        encoded.append(a)
    elif '"' in line and '\\' not in line:
        a = line.replace('"','\\"')
        a = '\"{}\"'.format(a)
        encoded.append(a)
    elif '\\' in line and '"' in line:
        a = line.replace('\\','\\\\')
        b = a.replace('"','\\"')
        b = '\"{}\"'.format(b)
        encoded.append(b)

print sum([len(line) for line in encoded])-sum([len(line) for line in n])

