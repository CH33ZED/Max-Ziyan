import time

def timer(f):
    start = time.time()
    f()
    end = time.time()
    print end - start
    return f

@timer
def funct():
    time.sleep(2)
    return "done"

print funct()

def nameandargs(f):
    name = f.func_name
    def inner(*arg):
        print name + " " + f(*arg)
        return name + " " + f(*arg)
    return inner
@nameandargs
def functwithargs(a, b, c):
    print a + "1"
    print b + "2"
    print c + "3"
    return "done"

print functwithargs("one", "two", "three")

