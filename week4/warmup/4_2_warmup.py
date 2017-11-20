import datetime as dt

class TimeStamp(object):
    def set_time(self):
        self.timestamp = str(dt.datetime.now())
    def get_time(self):
        return self.timestamp

var1 = TimeStamp()
var2 = TimeStamp()

var1.set_time()
var2.set_time()
print 'var1 get_time:', var1.get_time()
print 'var2 get_time:', var2.get_time()
print
var1.set_time() # change timestamp for var1
print 'var1 get_time:', var1.get_time()
print 'var2 get_time:', var2.get_time()
