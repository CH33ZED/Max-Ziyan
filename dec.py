import time

def timer(f):
    start = time.time()
    f()
    end = time.time()
    print "time:"
    print end - start
    return f

@timer
def funct():
    time.sleep(2)
    return "done1"

print funct()

def nameandargs(f):
    name = f.func_name
    def inner(*arg):
        print "function name: " + name
        print str([x for x in arg])
        return f(*arg)
    return inner

@nameandargs
def functwithargs(a, b, c):
    return "done2"

print functwithargs("one", "two", "three")

