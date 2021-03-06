import re
import itertools
#cleans up the raw text input to guest-operator-value-guest
def clean_input(x):
    remove = re.compile(' happiness units by sitting next to')
    remove2 = re.compile(' would')
    y = [remove2.sub("",item) for item in [remove.sub("",item) for item in x]]
    return y
# finds the possible combinations of guests from the raw text file
def find_guest_combos(x,want_permutes):
    guests = set()
    me = "Matt"
    matches = [re.findall('[A-Z]\w+',item) for item in x]
    for item in matches:
        for guest in item:
            guests.add(guest)
            guests.add(me)
    if want_permutes == 'y':
        return list(itertools.permutations(guests))
    elif want_permutes == 'n':
        return guests
    else:
        print 'You need to specity \'y\' or \'n\' for the second argument.'
        return None
# takes the cleaned input and builds a dictionary of possible people-people happiness values
def make_pairs(x):
    pairs = {}
    for instructions in x:
        #pi = parsed instructions
        pi = re.findall('[\w]+',instructions)
        if 'lose' in pi:
            pairs[(pi[0],pi[3])] = -int(pi[2])
        else:
            pairs[(pi[0],pi[3])] = int(pi[2])
    aa = find_guest_combos(x,'n')
    ab = "Matt"
    ac = [(item,ab) for item in aa]
    ad = [(ab,item) for item in aa]
    for item in ac:
        pairs[item] = 0
    for item in ad:
        pairs[item] = 0
    return pairs
#using the e-guest-harmony algorithm (patent not pending), finds the most optimal combination of table guests.
#takes two arguments - the dictionary returned from make_pairs, and the list of possible combinations from find_guest_combos
def e_guest_harmony(x,y):
    mylist = []
    for possible_combo in y:
        combo_sum = 0
        a = zip(possible_combo,possible_combo[1:])
        c = possible_combo[0],possible_combo[(len(possible_combo)-1)]
        d = possible_combo[(len(possible_combo)-1)],possible_combo[0]
        combo_sum += x[c] + x[d]
        for pair in a:
            b = pair[1],pair[0]
            combo_sum += x[pair] + x[b]
        mylist.append(combo_sum)
    return max(mylist)

def main():
    try:
        m = open('input.txt','r+').read().splitlines()
        clean_instructions = clean_input(m)
        a = find_guest_combos(m,'y')
        b = make_pairs(clean_instructions)
        print e_guest_harmony(b,a)
    except IOError:
        print 'Could not open the file.'

if __name__ == "__main__":
    main()