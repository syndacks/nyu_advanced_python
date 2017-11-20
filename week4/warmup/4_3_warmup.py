import datetime as dt

class TimeStamp(object):
    def __init__(self):
        self.timestamp = str(dt.datetime.now())
    def get_time(self):
        return self.timestamp

var1 = TimeStamp()
var2 = TimeStamp()

var1.get_time()
var2.get_time()
print 'var1 get_time:', var1.get_time()
print 'var2 get_time:', var2.get_time()
print '---------------'
print 'var1 get_time:', var1.get_time()
print 'var2 get_time:', var2.get_time()
