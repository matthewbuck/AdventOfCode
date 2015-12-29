m = open('input.txt','r+')
n = m.read().splitlines()[:1]

# set up 10^1x10^1 array - debug only fix in real test
grid = [[0 for x in range(10)] for x in range(10)]

# splitting functions
def split_instructions(x):
    x = x.split()
    print x
    return x

def int_split(f,s):
    f = f.split(',')
    s = s.split(',')
    fx = f[0]
    fy = f[1]
    sx = s[0]
    sy = s[1]
    return fx,fy,sx,sy

#processing functions
#ct stands for coordinate tuple
def turn_on(ct):
    return 0
def turn_off(ct):
    return 0
def toggle(ct):
    return 0

def home(x):
    if x[0] == 'turn':
        if x[1] == 'on':
            mt = int_split(x[3],x[5])

        else:
            mt = int_split(x[3],x[5])
    elif x[0] == 'toggle':
        mt = int_split(x[1],x[4])

#test github desktop 3
#test github laptop 3



print n
print map(split_instructions,n)