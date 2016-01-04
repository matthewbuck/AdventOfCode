m = open('test.txt','r+')
n = m.read().splitlines()[:5]
# this list contains an index and a tuple with the length of the item and it's actual text.
# i now need to create something that 'processes' the strings like the interpreter would...
# i could write a 'interpreter' that just does what the interpreter would do i.e it would remove the quotes, ignore
# things after the escape, etc., then compute the length of that and put it in an enumerated list, and somehow combine
# the two lists to do the math...
# shit no it can....but it's combining things in a weird way...why is it sometimes adding a slash?
# it's doing it in n... weird
y = list(enumerate([(len(item),item) for item in n]))
z = list(enumerate([(len(eval(item)),eval(item)) for item in n]))

#debug
print n
print y
print z

