#def problema_14(start):
    #current = 1
    #longest = 1

    #while start > 1:
        #start -= 1
        #nr = start
        #length = 1

        #while nr != 1:
            #if nr % 2 == 0:
                #nr = nr / 2
            #else:
                #nr = (nr * 3) + 1
            #length += 1

        #if current < length:
            #longest = start
            #current = length

    #return longest

#if __name__ == "__main__":
    #print problema_14(1000000)

collatz = {1:1}
def Collatz(n):
    global collatz
    if not collatz.has_key(n):
        if n%2 == 0:
            collatz[n] = Collatz(n/2) + 1
        else:
            collatz[n] = Collatz(3*n + 1) + 1
    return collatz[n]

for j in range(1000000,0,-1):
    Collatz(j)

print collatz.keys()[collatz.values().index(max(collatz.values()))]