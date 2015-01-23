import sys
import time

def greedy(max):
    res = 0

    def fib(m):
        a, b = 1, 2
        yield a
        yield b
        while 1:
            a, b = b, a + b
            if b >= m:
                return
            yield b

    for x in fib(max):
        if x % 2 == 0:
            res += x
    return res


def opt(max):
    def fib(m):
        a, b = 1, 2
        yield b
        while 1:
            a, b = b, a + b
            if b >= m:
                return
            if not b % 2:
                yield b
    return sum(fib(max))

def zopt(max):
    x = y = 1
    sum = 0
    while (sum < max):
        sum += (x + y)
        x, y = x + 2 * y, 2 * x + 3 * y
    return sum

if __name__ == "__main__":
    args = sys.argv
    a = args[1] if len(args) > 1 else 7

    print "Greedy"
    start = time.time()
    print greedy(int(a))
    print time.time() - start

    print "Opt 1"
    start = time.time()
    print opt(int(a))
    print time.time() - start

    print "Opt 2"
    start = time.time()
    print zopt(int(a))
    print time.time() - start
