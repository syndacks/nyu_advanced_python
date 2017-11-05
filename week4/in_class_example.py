class MyClass(object):
    """in class exercise"""
    def __init__(self):
        self.innerlist = []

    def append(self, arg):
        self.innerlist.append(arg)


x = MyClass()
x.append(1)
print(x.innerlist)
