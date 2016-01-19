def password_refresh(pw):
    pw = [x for x in pw][::-1]
    for idx,char in enumerate(pw):
        if char == 'z':
            pw[idx] = 'a'
        else:
            pw[idx] = chr(ord(char)+1)
            break
    return ''.join(pw)[::-1]

def function1(pw):
    if 'i' in pw or 'o' in pw or 'l' in pw:
        return False
    else:
        return True

def function2(pw):
    doublecount = 0
    duplicates = ''
    for idx,char in list(enumerate(pw))[:len(pw)-1]:
        thischar = char
        nextchar = pw[idx+1]
        if thischar == nextchar and thischar not in duplicates:
            doublecount += 1
            duplicates += str(thischar) + str(nextchar)
        else:
            continue
    if doublecount == 2:
        return True
    else:
        return False

def function3(pw):
    for idx,char in list(enumerate(pw))[:len(pw)-2]:
        thischar = char
        nextchar = pw[idx+1]
        thirdchar = pw[idx+2]
        if nextchar == chr(ord(thischar)+1) and thirdchar == chr(ord(thischar)+2):
            return True
        else:
            continue
        return False

def is_valid_pw(pw):
    badpassword = True
    while badpassword:
        pw = password_refresh(pw)
        if function1(pw):
            if function2(pw):
                if function3(pw):
                    badpassword = False
                    return pw
                else:
                    continue
            else:
                continue
        else:
            continue

def main():
    x = raw_input('Enter the current password:')
    a = raw_input('Enter the number of passwords you want to generate:')
    a = int(a)
    for turns in range(a):
        y = is_valid_pw(x)
        print 'The next password is {}.'.format(y)
        x = y
    return None

if __name__ == '__main__':
    main()