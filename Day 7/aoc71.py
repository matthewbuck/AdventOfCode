m = open('input.txt','r+')
n = m.read().splitlines()

def break_up_lines(x):
    return [lines.strip().split(' -> ') for lines in x]

wiregrid = {}

def find_wire_inputs(x):
    for line in x:
        if line[0].isdigit():
            wiregrid[line[1]] = int(line[0])
        else:
            pass

def process_others(x):
    for line in x:
        if 'OR' in line[0]:
            q = line[0].split(' OR ')
            if q[0] in wiregrid and q[1] in wiregrid:
                a = wiregrid[q[0]]
                b = wiregrid[q[1]]
                c = a | b
                wiregrid[line[1]] = c
        elif 'LSHIFT' in line[0]:
            q = line[0].split(' LSHIFT ')
            if q[0] in wiregrid:
                a = wiregrid[q[0]]
                b = int(q[1])
                c = a << b
                wiregrid[line[1]] = c
        elif 'RSHIFT' in line[0]:
            q = line[0].split(' RSHIFT ')
            if q[0] in wiregrid:
                a = wiregrid[q[0]]
                b = int(q[1])
                c = a >> b
                wiregrid[line[1]] = c
        elif 'NOT' in line[0]:
            q = line[0].split('NOT ')
            if q[1] in wiregrid:
                a = wiregrid[q[1]]
                b = ~ a
                c = b & 0xffff
                wiregrid[line[1]] = c
        elif 'AND' in line[0]:
            q = line[0].split(' AND ')
            if q[0].isdigit():
                if q[1] in wiregrid:
                    a = wiregrid[q[1]]
                    b = 1
                    c = a & b
                    wiregrid[line[1]] = c
                else:
                    pass
            elif q[0].isalpha():
                if q[0] in wiregrid and q[1] in wiregrid:
                    a = wiregrid[q[0]]
                    b = wiregrid[q[1]]
                    c = a & b
                    wiregrid[line[1]] = c
                else:
                    pass
            else:
                pass
        else:
            #this is a direct assignment
            if line[1] in wiregrid:
                pass
            else:
                if line[0] in wiregrid:
                    c = wiregrid[line[0]]
                    wiregrid[line[1]] = c
                else:
                    pass
    if 'a' in wiregrid:
        pass
    else:
        process_others(x)

    return 'The signal on \'a\' is {}.'.format(wiregrid.get('a'))

def main():
    u = break_up_lines(n)
    find_wire_inputs(u)
    h = process_others(u)
    print h

if __name__ == '__main__':
    main()














