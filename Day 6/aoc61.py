m = open('input.txt','r+')
n = m.read().splitlines()[:1]

grid = [[0 for x in range(1000)] for x in range(1000)]

# splitting functions
def split_instructions(x):
    x = x.split()
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
    fx = int(ct[0])
    fy = int(ct[1])
    sx = int(ct[2])
    sy = int(ct[3])
    xdiff = sx-fx
    ydiff = sy-fy
    for lights in range(ydiff):
        for lights in range(xdiff):
            grid[fx][fy] = 1
            fx += 1
        fy += 1

def turn_off(ct):
    return 0
def toggle(ct):
    return 0

def light_it(x):
    #instr = split_instructions(x)
    if x[0][0] == 'turn':
        if x[0][1] == 'on':
            print 'hey'
            turn_on(int_split(x[0][2],x[0][4]))
        else:
            mt = int_split(x[3],x[5])
    elif x[0] == 'toggle':
        mt = int_split(x[1],x[4])
    print grid.count(1)

z = map(split_instructions,n)
print z[0]
print z[0][0]
print z[0][4]
light_it(z)
