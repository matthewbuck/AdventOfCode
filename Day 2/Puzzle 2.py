f = open('input.txt','r+')
m = f.read()

m = m.splitlines()
print m

def calc_ribbon(box):
    d = box.split('x')
    d[0] = int(d[0])
    d[1] = int(d[1])
    d[2] = int(d[2])
    px = 2*d[0]+2*d[1]
    py = 2*d[1]+2*d[2]
    pz = 2*d[2]+2*d[0]

    sp = min(px,py,pz)
    bv = d[0]*d[1]*d[2]
    return sp+bv

val = map(calc_ribbon,m)
val = sum(val)
print val


