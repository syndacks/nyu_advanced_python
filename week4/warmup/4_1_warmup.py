class ThisClass(object):
    def ID(self):
        return id(self)

    def report(self):
        print self.ID()


a = ThisClass()
b = ThisClass()
c = ThisClass()

a.report()
b.report()
c.report()

print(id(a)) # same as a ID
print(id(b)) # same as b ID
print(id(c)) # same as c ID
