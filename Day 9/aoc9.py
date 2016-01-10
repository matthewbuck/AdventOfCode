import itertools
import re

def process_input_file(x):
    m = open('{}.txt'.format(x),'r')
    n = m.read().splitlines()
    return n

def split_into_uniques(x):
    x = tuple(tuple(x) for x in tuple(
            [line.split(' to ') for line in [line[0] for line in [line.split(' = ') for line in x]]]))
    l = set()
    for line in x:
        l.update(line)
    return l

def create_combinations(x):
    return list(itertools.permutations(x))

def create_dict(x):
    citydict = {}
    for line in x:
        a = re.findall('[\w]+',line)
        a.remove('to')
        q = (a[0],a[1])
        r = (a[1],a[0])
        s = (a[2])
        citydict[q] = s
        citydict[r] = s
    return citydict

def eval_maps(uniquecombos,localdict):
    distances = []
    for item in uniquecombos:
        s = 0
        for pair in zip(item,item[1:]):
            a = int(localdict[pair])
            s += a
        distances.append(s)
    print "The minimum distance is {}. The maximum distance is {}.".format(min(distances),max(distances))

def main():
    x = raw_input('Type \"test\" to run the test file, \"input\" to run the input file.')
    try:
        file = process_input_file(x)
        localdict = create_dict(file)
        file = create_combinations(split_into_uniques(file))
        eval_maps(file,localdict)
    except IOError:
        print 'Your entry is invalid. Please try again.'
        main()

if __name__ == '__main__':
    main()