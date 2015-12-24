m = open('input.txt','r+')
n = m.read()
n = n.splitlines()

def eval_string(x):
    c = False
    disallowed = ['ab','cd','pq','xy']
    y = [1 for letter in x if letter in 'aeiou']
    if len(y) >= 3:
        a = [1 for item in disallowed if item in x]
        if len(a) == 0:
            for n in range(len(x)-1):
                if x[n] == x[n+1]:
                    c = True
                else:
                    pass
    if c:
        return 'Nice'
    else:
        return 'Naughty'

counter = 0
for l in n:
    if eval_string(l) == 'Nice':
        counter +=1
print counter
