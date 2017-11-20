class MaxSizeList(object):
    def __init__(self, max_size):
        self.list = []
        self.max_size = max_size

    def push(self, item):
        self.list.append(item)
        if len(self.list) > self.max_size:
            self.list.pop()

    def get_list(self):
        return self.list


a = MaxSizeList(3)
b = MaxSizeList(1)
a.push("hey")
a.push("ho")
a.push("let's")
a.push("go")
b.push("hey")
b.push("ho")
b.push("let's")
b.push("go")
print a.get_list() # ['ho', "let's", 'go']
print b.get_list() # ['go']
