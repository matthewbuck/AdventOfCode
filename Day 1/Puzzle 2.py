f = open('input.txt','r+')
mytext = f.read()

counter = 0
position = 0

for char in mytext:
    if counter >=0:
        if char == '(':
            counter+=1
            position+=1
        elif char == ')':
            counter-=1
            position+=1
    else:
        print position
        break