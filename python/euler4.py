import sys
import time

def greedy(max):
    max = 0
    count = 0
    for x in reversed(range(100, 1000)):
        for y in reversed(range(100, 1000)):
            count += 1
            m = str(x * y)
            if m == m[::-1]:
                m = int(m)
                if m > max:
                    max = m
    print "Count %s" % count
    return max

def opt(max):
    max = 0
    count = 0
    for x in reversed(range(100, 1000)):
        for y in reversed(range(x, 1000)):
            count += 1
            m = x * y
            if m < max:
                 break
            if str(m) == str(m)[::-1]:
                if m > max:
                    max = m
    print "Count %s" % count
    return max

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
