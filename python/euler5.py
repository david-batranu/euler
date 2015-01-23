import sys
import time

def primes(max):
    prime = []
    for x in range(2, max+1):
        for y in range(2, x):
            if x % y == 0:
                break
        else:
            prime.append(x)
    return prime

def opt(max):

    remaining = range(2, max)
    pr = primes(max)

    res = 1
    for x in pr:
        res *= x

    def cleanup(remaining, pr):
        # Remove prime numbers
        remaining = sorted(set(remaining).difference(pr))

        for x in pr:
            for y in pr:
                if y <= x:
                    continue
                if y % x == 0:
                    continue
                z = x * y
                if z > max:
                    break
                if z in remaining:
                    remaining.remove(z)
        return remaining

    remaining = cleanup(remaining, pr)
    found = False

    while remaining:

        # Add more primes
        for x in remaining:
            for y in pr:
                if x % y == 0:
                    pr.append(x)
                    pr = sorted(pr)
                    found = True
                    res *= y
                    break
            if found:
                remaining = cleanup(remaining, pr)
                break

    return res

def greedy(max):
    pr = primes(max)

    start = 1
    for x in pr:
        start *= x

    res = start
    # return res * 8 * 3

    while True:
        found = True
        for x in range(2, max+1):
            if res % x:
                found = False
                break
        if found:
            break
        res += 1
    return res

def zopt(max):
    def divisible(a):
        for i in range(1, max):
            if a % i == 0:
                x = True
            else:
                x = False
                break
        return x

    n = max
    while divisible(n) == False:
        n += max
    return n

if __name__ == "__main__":
    args = sys.argv
    a = args[1] if len(args) > 1 else 7

    print "\nGreedy\n"
    start = time.time()
    # print greedy(int(a))
    print time.time() - start

    print "\nOpt 1\n"
    start = time.time()
    print opt(int(a))
    print time.time() - start

    print "\nOpt 2\n"
    start = time.time()
    print zopt(int(a))
    print time.time() - start
