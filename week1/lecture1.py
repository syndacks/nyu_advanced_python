# #homework due on Sunday nights
# >>> y = []
# >>> type(y)
# <type 'list'>
# >>> dir(y)
# ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# while loops can be helpful for thins that if elif else are not good for
while True:
    ui = input('please enter an integer: ')
    if not ui.isdigit():
        continue
    uii = int(ui)
    break

# what are the types of each line?

#
mysum = 0.0
mycount = 0
# this is a link to the file
fh = open('mytabularfile.csv')
# line is a string
for line in fh:
    # items is a list
    items = line.split(',')
    # wanted_val is a string
    wanted_val = items[3]
    # iwant is an integer
    iwant = int(wanted_val)
    # mysum is a float
    mysum = mysum + iwant
    # mycount is
    mycount = mycount + 1

# other ways of opening files
fh = open('mytabularfile')
text = fh.read() #returns an single string

fh = open('mytabularfile')
lines = fh.readlines() #returns an array

'atomic types': (int, float, str)
# you can check for membership e.g. for blah in list:
'container types': (list, dict, tuple, set)
'boolean types'
'nonetype type'


x = {'a': 1, 'b':2, 'c':3}
#set
z = {1,2,3,4,5}
