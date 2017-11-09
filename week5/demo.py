import random

class MyClass(object):
    classval = 'hey!'
    counter = 0
    def __init__(self):
        self.objval = random.randint(1,5)
    def __iter__(self):
        print 'now in iter'
        self.counter = 0
        return self
    def next(self):
        self.counter += 1
        if self.counter > 4:
            raise StopIteration
        return self.counter

# this is how you iterate over things in Classes
# when you use for in an object, it calls __iter__
# then next gets called (multiple times)
obj = MyClass()
obj2 = MyClass()
# item is whatever gets returned in next
for item in obj:
    print item

print 'looping a second time'

for item in obj2:
    print item

print obj.classval
print obj2.classval

print obj.objval
print obj2.objval
