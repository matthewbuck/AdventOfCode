def lookandsay(input,times):
    times = int(times)
    while times > 0:
        target = input[0]
        others = input[1:]+ " "
        count = 1
        string = ''
        for item in others:
            if item == target:
                count += 1
            else:
                string += str(count) + str(target)
                target = item
                count = 1
        times -= 1
        input = string
    return len(string)

def main():
    x = raw_input('Enter the number you want to play the game with.')
    y = raw_input('Enter the number of times you want to play.')
    if type(x) == type('') and y.isdigit():
        print lookandsay(x,y)
    else:
        print 'You entered one of the variables incorrectly. Try again.'
        main()

if __name__ == '__main__':
    main()