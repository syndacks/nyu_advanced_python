def logger(function):
    def wrapper(*args, **kwargs):
        print "entering:", function.__name__
        function(*args)
        print "exiting:", function.__name__
    return wrapper

@logger
def greet(person):
    print 'hello, {}!'.format(person)

greet('dacks')
# entering: greet
# hello, dacks!
# exiting: greet
