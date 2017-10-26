def doubleit(x):
    return x * 2

def myfunc4(myfunc):
    z = myfunc(5)
    return z

myfunc4(doubleit)


# good to use this instead of a bunch of iff statements
dispatch = {'double': doubleit, 'triple':tripleit, 'quadruple':lambda x: x*4}
