import hashlib

def find_hash(key,zeroes):
    x = 0
    continueon = True
    mval = ''.join(['0' for x in range(zeroes)])
    while continueon:
        m = hashlib.md5()
        m.update(key)
        m.update(str(x))
        n = m.hexdigest()
        if n.startswith('mval'):
            continueon = False
            print x
        else:
            x += 1
    return 0




