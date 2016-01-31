import json
count = 0
def switcheroo(myiter):
    global count
    for item in myiter:
        if type(item) == int:
            count += item
            continue
        elif type(item) == unicode:
            continue
        elif type(item) == dict:
            if 'red' in item.itervalues():
                pass
            else:
                switcheroo(item.itervalues())
        elif type(item) == list:
            switcheroo(item)
    return count

def main():
    m = open('input.txt','r+')
    n = json.loads(m.read())
    m = switcheroo(n)
    print("The count was {}.".format(m))

if __name__ == "__main__":
    main()
