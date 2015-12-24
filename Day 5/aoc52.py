z = open('input.txt','r+')
k = z.read()
k = k.splitlines()

def eval_string_ii(x):
    c = False
    d = False
    for n in range(len(x)-2):
        if x[n] == x[n+2]:
            c = True
        else:
            pass
    for n in range(len(x)-1):
        t = x[n]+x[n+1]
        e = x.find(t,n+2,len(x))
        if e >0:
            d = True
        else:
            pass
    if c and d:
        return 'Nice'
    else:
        return 'Naughty'

count = 0
for part in k:
    if eval_string_ii(part) == 'Nice':
        count += 1
print count