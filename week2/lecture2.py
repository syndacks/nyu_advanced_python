# import os

# y = ['a', 'b', 'c']
# x = [1, 2, 3]
# x.append(y)
# print x
#
# x[3].append('d')
#
# print y


# outerdict = {
#     '/mydir/test.txt' : {
#         'name': "Dacks1",
#         'size': 123
#     },
#     '/mydir/test2.txt' : {
#         'name': "Dacks2",
#         'size': 456
#     }
# }
#
# for key in outerdict:
#     print key
#     print outerdict[key]['size']
#
# # this is not the same as:
#
# for key in outerdict:
#     for inner_key in key:
#         print inner_key
#

#oh-my-zsh

# from pprint import pprint
# lines = """client1,sunday,10.50
# client2,sunday,20
# client3,monday,11.25
# client1,monday,24
# client3,tuesday,42
# client1,thursday,11""".splitlines()
# cd = {}
# for line in lines:
#     client, day, amt = line.split(',')
#     if client not in cd:
#         cd[client] = []
#     cd[client].append(float(amt))
#
# pprint(cd)


def getlen(arg):
    return len(arg)

x = ['David', 'Joel', 'Zeb', 'Abagail']

sx = sorted(x, key=getlen)
print(sx)

#unwttng.com/what-is-a-blockchain

# 1 - what is one item to be sorted?
# 2 - what value would have that item to be sorted?
# 3 - can i write a function that takes 1 and returns 2?


def bylastval(arg):
    return x[arg][2]

x = {
    'David': [1,2,3],
    'Joel': [2, 10, 4],
    'Zeb': [3, 5, 6]
    }

sx = sorted(x, key=bylastval)
print sx
# to get around the global: use a lambda or use a tuple (?)
