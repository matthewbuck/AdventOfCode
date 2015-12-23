f = open('input.txt','r+')
m = f.read()

m = m.splitlines()

def calc_paper(box):
    d = box.split('x')
    d[0] = int(d[0])
    d[1] = int(d[1])
    d[2] = int(d[2])
    x = d[0]*d[1]
    y = d[1]*d[2]
    z = d[2]*d[0]

    sa = 2*x+2*y+2*z
    ss = min(x,y,z)
    tp = sa+ss
    return tp

val = sum(map(calc_paper,m))
print val





