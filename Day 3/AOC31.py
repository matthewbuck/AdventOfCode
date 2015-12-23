f = open('input.txt','r+')
o = f.read()
    
def coordinates(stri):
    x = 0
    y = 0
    table = []
    for direction in stri:
        if direction == "^":
            y += 1
            entry = '%s,%s'%(x,y)
            table.append(entry)
        elif direction == "v":
            y -= 1
            entry = '%s,%s'%(x,y)
            table.append(entry)
        elif direction == ">":
            x += 1
            entry = '%s,%s'%(x,y)
            table.append(entry)
        elif direction == "<":
            x -= 1
            entry = '%s,%s'%(x,y)
            table.append(entry)
        else:
            pass
    ntable = []
    for coordinate in table:
        if coordinate not in ntable:
            ntable.append(coordinate)
        else:
            pass

    return len(ntable)+1

print coordinates(o)


