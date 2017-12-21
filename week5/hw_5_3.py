class AttrType(object):
    def __init__(self, _type):
        self._type = _type
        # print "self from init", self.__dict__
        # print "_type from init", self._type

    def __getattribute__(self, name):
        object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        print "self from __setattr__: ", self.__dict__

        object.__setattr__(self, attrname, attrvalue)
        if isinstance(object.__getattribute__, self._type) is False:
            print "fuck"


x = AttrType(int)
x.a = 10
print x.a
print x._type
