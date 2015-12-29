m = open('input.txt','r+')
n = m.read().splitlines()

grid = [[0 for x in range(1000)] for y in range(1000)]
#should probably package into multiple smaller functions
def light_it(x):
    for line in n:
        if line.startswith('turn on'):
            firstval = line.split()[2]
            secondval = line.split()[4]
            t = (firstval.split(','), secondval.split(','))
            x1 = int(t[0][0])
            y1 = int(t[0][1])
            x2 = int(t[1][0])
            y2 = int(t[1][1])
            for xsteps in range(x1,x2+1):
                for ysteps in range(y1,y2+1):
                    grid[xsteps][ysteps] = 1
        elif line.startswith('turn off'):
            firstval = line.split()[2]
            secondval = line.split()[4]
            t = (firstval.split(','), secondval.split(','))
            x1 = int(t[0][0])
            y1 = int(t[0][1])
            x2 = int(t[1][0])
            y2 = int(t[1][1])
            for xsteps in range(x1,x2+1):
                for ysteps in range(y1,y2+1):
                    grid[xsteps][ysteps] = 0
        elif line.startswith('toggle'):
            firstval = line.split()[1]
            secondval = line.split()[3]
            t = (firstval.split(','),secondval.split(','))
            x1 = int(t[0][0])
            y1 = int(t[0][1])
            x2 = int(t[1][0])
            y2 = int(t[1][1])
            for xsteps in range(x1,x2+1):
                for ysteps in range(y1,y2+1):
                    if grid[xsteps][ysteps] == 0:
                        grid[xsteps][ysteps] = 1
                    elif grid[xsteps][ysteps] == 1:
                        grid[xsteps][ysteps] = 0

    total = 0
    error_total = 0
    error_total_2 = 0
    for row in grid:
        total += row.count(1)
    for row in grid:
        error_total += row.count(2)
    for row in grid:
        error_total_2 += row.count(-1)
    return '{} lights are turned on. {} lights came back as a two, {} lights came back as -1'.format(total,error_total,error_total_2)


print light_it(n)
