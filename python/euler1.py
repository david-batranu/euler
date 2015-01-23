import sys
import time

def greedy(x):
    res = 0
    for y in range(0, x):
        if y % 3 == 0:
            res += y
        elif y % 5 == 0:
            res += y
    return res

def opt1(x):
    res = 0
    for y in iter(range(0, x, 3)):
            res += y
    for y in iter(range(0, x, 5)):
        if y % 3 == 0:
            continue
        res += y
    return res

def opt2(x):
    res = 0

    y = 0
    while y < x:
        y += 3
        res += y

    y = 0
    while y < x:
        y += 5
        if not y % 3:
            continue
        res += y

    return res

if __name__ == "__main__":
    args = sys.argv
    a = args[1] if len(args) > 1 else 7

    print "Greedy"
    start = time.time()
    print greedy(int(a))
    print time.time() - start

    print "Opt 1"
    start = time.time()
    print opt1(int(a))
    print time.time() - start

    print "Opt 2"
    start = time.time()
    print opt2(int(a))
    print time.time() - start
