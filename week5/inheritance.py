# class inheritance
# class ZClass(dict):
#     def __setitem__(self, key, val):
#         pass
#
# x = ZClass()
# x['a'] = 5
# x['b'] = 10
#
# print(x)

"""class ZClass(dict):
    def __setitem__(self, key, val):
        if not isinstance(val, int):
            raise TypeError('value must be int')
        dict.__setitem__(self, key, val)

x = ZClass()
x['a'] = 5
x['b'] = 10
print(x)

for key, val in x.items():
    print(key, val)

x['c'] = 'hello'"""

class ZClass(dict):
    def __init__(self):
        self.md = {}
    # when you try to set the value of an object, you use setattr
    def __setattr__(self, key, val):
        print "calling setattr"
        print "key from setattr", key, "val from setattr", val
    # when you try to get the value of an object, you use getatt
    def __getattr__(self, key):
        print "calling getattr"
        print "key from getattr", key

x = ZClass()
# self is x, x is self
# self.a calls set attr
x.a = 5
print x.a
