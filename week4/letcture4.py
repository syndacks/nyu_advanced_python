# Entering the next phase of the course, which is on Classes
# function - named routine
# class - helps us create an object of that class (an instance)
# an object is an instance of a particular type with access to characteristic functionality
#   and it's own data.
# classes allows us to sequester complexity behind an interface we defince


# how is this differnt than a dictionary? b/c dictionaries are tied to the class dictionary
# where as these classes you can control
# classes are smart data
class MyInt(object):
    """fuck"""


x = MyInt()
x.vara = 5
print x.vara

y = MyInt()
y.vara = 500
print y.vara
print x.vara

exit()

"""
class MyInt(object):
    ''' a class for demo purposes '''
    def setval(self, obj):
        print(id(self))
        self.innerval = obj

    def getval(self):
        return self.innerval

# we are really passing two arguments to setval, but it looks like we are only passing one
# the first value we are passing is realyly self
x = MyInt()
print(id(x))
x.setval(10)                # MyInt.setval(x, 10)
print x.getval()            # MyInt.getal(x)

y = MyInt()
print id(y)
y.setval(10)                # MyInt.setval(x, 10)
"""
