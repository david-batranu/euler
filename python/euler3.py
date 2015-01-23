import sys
import time

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n /= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac

def greedy(max):
    return primes(max)

def opt(max):
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
